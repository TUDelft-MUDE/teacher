# `mude` Setup

To modify the server setup, SSH into `mude.citg.tudelft.nl`. You can use the command below:

```bash
sudo nano /var/web_server/website_docker_configuration/default.conf
```

```
location /archive {
        alias /var/www/html/archive;
        index index.html index.htm intro.html;
        try_files $uri $uri/ =404;
}
location /incoming {
        alias /var/www/html/incoming;
        index index.html index.htm intro.html;
        try_files $uri $uri/ =404;
}
location /teacher {
        alias /var/www/html/teacher;
        index index.html index.htm inro.html;
        try_files $uri $uri/ =404;
}
```

This is the example of the subdomain:
- mude.citg.tudelft.nl/archive
- mude.citg.tudelft.nl/incoming
- mude.citg.tudelft.nl/teacher

All you need to do to set up the new subdomain is to write exactly as the example shows.

### Configuration Details

#### Alias
```nginx
alias /var/www/html/{domain name};
```
This sets the alias for the `/ {domain name}` location to the directory `/var/www/html/{domain name}`. When a request matches `/ {domain name}`, Nginx serves the files from this directory.

If you `cd /var/www/html`, you could see nothing except the default Nginx `index.html` file on the `mude.citg.tudelft.nl` Linux server. This is because the server is using a proxy. `/var/web_server/htdocs/` is where the actual contents stay.

#### Index Files
```nginx
index index.html index.htm intro.html;
```
This specifies the default files to serve if a directory is requested. Nginx will look for `index.html`, `index.htm`, or `intro.html` in that order.

To add a new subdomain and `index.html` for the new website, use the command:
```bash
cd /var/web_server/htdocs/
sudo mkdir {domain name}
sudo nano {domain name}/index.html
```

Write down anything in the `index.html` file. Press `(Ctrl+X -> Y)` to save and exit from the nano text editor. In this way, your `index.html` file will be created successfully.

#### Try Files
```nginx
try_files $uri $uri/ =404;
```
This directive attempts to serve the requested URI as a file or a directory. If neither exists, it returns a 404 error.

### Restarting Docker

After you finish the setup above, you need to restart the Docker container with the following commands:

1. Check if the configuration is correct:
    ```bash
    sudo docker exec website_docker_configuration-nginx-1 nginx -t
    ```

    ```
    nginx: the configuration file /etc/nginx/nginx.conf syntax is ok
    nginx: configuration file /etc/nginx/nginx.conf test is successful
    ```

    If it shows this, then it is well done.

2. If the test is successful, reload Nginx:
    ```bash
    sudo docker exec website_docker_configuration-nginx-1 nginx -s reload
    ```

    ```
    [notice] 36#36: signal process started
    ```

    This message means the server is successfully reloaded.

Now you can navigate to `mude.citg.tudelft.nl/{domain name}` to test your new website!

## **Webhook Deployment**

Instead of using direct SSH access for deploying files, GitLab provides a service called "Webhook." This allows us to automatically deploy files from the GitLab repository and execute bash scripts on the webserver to build and update the website.

For instance, a webhook configuration file can be found at **`/etc/webhook/hooks.json`**. Below is an example of such a configuration:

```
  {
    "id": "book-deploy-draft",
    "execute-command": "/srv/webhook/deploy_book_artifact.sh",
    "pass-arguments-to-command": [
      {
        "source": "payload",
        "name": "object_attributes.ref"
      },
      {
        "source": "string",
        "name": "book/_build/html"
      },
      {
        "source": "string",
        "name": "/var/web_server/htdocs/2024/book-draft"
      },
      {
        "source": "string",
        "name": "ACCESS TOKEN"
      },
      {
        "source": "payload",
        "name": "build_job_id"
      },
      {
        "source": "string",
        "name": "mude/book"
      }
    ],
    "trigger-rule": {
      "and": [
        {
          "match": {
            "type": "value",
            "value": "pipeline",
            "parameter": {
              "source": "payload",
              "name": "object_kind"
            }
          }
        },
        {
          "match": {
            "type": "value",
            "value": "success",
            "parameter": {
              "source": "payload",
              "name": "object_attributes.status"
            }
          }
        },
        {
          "match": {
            "type": "value",
            "value": "main",
            "parameter": {
              "source": "payload",
              "name": "object_attributes.ref"
            }
          }
        },
        {
          "match": {
            "type": "value",
            "value": "ACCESS TOKEN",
            "parameter": {
              "source": "header",
              "name": "X-Gitlab-Token"
            }
          }
        }
      ]
    },
    "trigger-rule-mismatch-http-response-code": 200
  }
```
This configuration defines a webhook event, book-deploy-draft, which triggers the execution of a shell script (/srv/webhook/deploy_book_artifact.sh) when a webhook is received from GitLab.

### Key Points:
- The placeholder "ACCESS TOKEN" should be replaced with the actual token you create (instructions on creating the token are provided below).
- This webhook is triggered when a pipeline on the main branch successfully completes.
It deploys the book draft from the directory book/_build/html to /var/web_server/htdocs/2024/book-draft.
- The webhook service can be configured in **`GitLab -> Settings -> Webhooks`**.

### Setting Up the Webhook
To set up the webhook service, follow these steps:

1. Create a Personal Access Token
Navigate to GitLab -> Settings -> Access Tokens and create a new token. The scopes and role should match the following example, while other details (like name and expiration date) can be customized.

| Token Name           | Scopes                    | Created       | Last Used   | Expires     | Role      |
|----------------------|---------------------------|---------------|-------------|-------------|-----------|
| Automatic deployment | read_api, read_repository  | Aug 30, 2024  | 11 hours ago | in 11 months | Developer |

2. Set Up the Webhook
Go to GitLab -> Settings -> Webhooks and add a new webhook with the following settings:

- URL: Enter the URL of your webhook, for example: https://mude.citg.tudelft.nl/hooks/book-deploy-draft (this should match the URL in your webhook configuration file).
- Secret Token: Paste the access token you created earlier into the "Secret Token" field.
- Trigger: Enable Pipeline events.
- SSL Verification: Ensure that SSL verification is enabled.
- Finally, click Add Webhook.

With these steps completed, your webhook will automatically trigger the deployment process whenever a successful pipeline runs on the main branch.

3. 






# `interactivetextbooks` setup
This has a GitLab CI/CD pipeline configuration file that automates the process of building a Docker image, pushing it to a Docker registry, and deploying it in a containerized environment. Here's a breakdown of the stages and commands:

### Stages
- **build**: This stage handles the creation and pushing of a Docker image.
- **deploy**: This stage handles deploying the built Docker image to a running container.

### Variables
- **`REGISTRY_HOST`**: Set to `localhost:5000`, representing the local Docker registry.
- **`TAG`**: This variable constructs a Docker image tag using the registry host, project name, and the branch name. The format is `localhost:5000/project_name/branch_name:latest`.

### Build Stage

1. **Image**: The pipeline uses the official Docker image to execute Docker commands.
2. **Rules**: The pipeline will only run this stage if the branch is `main` and the pipeline was triggered by a push event.
3. **Before script**: Runs `docker info` to confirm that Docker is working correctly.
4. **Script**:
   - `docker build -t $TAG .`: This builds a Docker image with the specified tag (`$TAG`) using the current directory as the build context.
   - `docker push $TAG`: Pushes the built Docker image to the local registry (`localhost:5000`).

### Deploy Stage

1. **Image**: Uses the Docker image again to handle container management.
2. **Rules**: This stage also runs only if the branch is `main` and the pipeline was triggered by a push event.
3. **Before script**:
   - `docker info`: Same as the build stage, checks Docker's status.
   - `docker stop $CI_PROJECT_NAME`: Attempts to stop any running container with the project name as the container name.
   - `if [ $exit_code -ne 0 ]; then echo "Container not found, cannot stop"; else docker rm $CI_PROJECT_NAME; fi`: If stopping the container fails (i.e., the container doesn't exist), a message is printed, but it continues execution. If successful, the container is removed.
4. **Script**:
   - `docker run -d --restart always -p 8007:80 --name $CI_PROJECT_NAME $TAG`: This runs the newly built and pushed Docker image as a container. The container is set to always restart, runs detached (`-d`), and exposes port `8007` on the host, forwarding it to port `80` in the container.

### Summary

- The pipeline is triggered on pushes to the `main` branch.
- In the **build** stage, it builds a Docker image and pushes it to a local Docker registry at `localhost:5000`.
- In the **deploy** stage, it stops and removes any existing container, then runs a new container with the built image, exposing port `8007` on the host machine.

# `SSL Certificate Setup` Guide
### Before You Begin

- **Authentication:** Use your NetID login credentials for all server access.
- **File Handling:** Commands assume copying, pasting, or transferring files to the current working directory.

### Generating CSR (Certificate Signing Request) on Webserver

-  **Create CSR File on Webserver:**
   - Follow [this guide](https://tu-delft-dcc.github.io/docs/infrastructure/VPS_SSL_Certs.html) to generate `.csr` and `.key` files on your webserver.

### Transferring CSR from Server to Local Machine

1. **Secure Copy (SCP) from Server to Local:**
   - Access the intermediary server:
     ```
     ssh {NetID}@student-linux.tudelft.nl or {NetID}@linux-bastion.tudelft.nl
     ```
   - Copy the `.csr` file from server to intermediary server:
     ```
     scp mude.citg.tudelft.nl:mude.citg.tudelft.nl.csr /home/nfs/{NetId}/
     ```

   - Copy the `.csr` file from intermediary server to your local machine:
     ```
     scp {NetID}@student-linux.tudelft.nl:/home/nfs/{NetID}/mude.citg.tudelft.nl.csr .
     ```

### Requesting SSL Certificate

1. **Submit CSR to TUDelft Top Desk:**
   - Visit [TUDelft Top Desk](https://www.tudelft.topdesk.net) and submit the `.csr` file to request your SSL certificate.

### Uploading PEM File to Webserver
- To figure out where the current cerficate exists, use the command below:
    ```
    sudo nano /etc/nginx/sites-available/mude
    ```
    ```
    server {
        # SSL configuration
        #
        listen 443 ssl http2;
        listen [::]:443 ssl http2;

        ssl_certificate /etc/ssl/certs/mude_citg_tudelft_nl.pem;
        ssl_certificate_key /etc/ssl/private/mude.citg.tudelft.nl.key;
    ```

    In this example, ssl_certificate and key are staying in (This key file should be created with the .csr)
    - /etc/ssl/certs
    - /etc/ssl/private

1. **SCP from Local Machine to Intermediary Server:**
   - Upload `.pem` file to intermediary server:
     ```
     scp mude.citg.tudelft.nl.pem {NetID}@student-linux.tudelft.nl:/home/nfs/{NetID}/
     ```

2. **SCP from Intermediary Server to Webserver:**
   - Access intermediary server:
     ```
     ssh {NetID}@student-linux.tudelft.nl
     ```
   - Transfer `.pem` file to webserver:
     ```
     scp /home/nfs/{NetID}/mude.citg.tudelft.nl.pem {NetID}@mude.citg.tudelft.nl:
     ```

### Updating SSL Certificate

   - Backup existing SSL files:
     ```
     sudo cp /etc/ssl/certs/mude_citg_tudelft_nl.pem /etc/ssl/certs/mude_citg_tudelft_nl.pem.bak
     sudo cp /etc/ssl/private/mude.citg.tudelft.nl.key /etc/ssl/private/mude.citg.tudelft.nl.key.bak
     ```

   - Replace with new `.pem` and `.key` files:
     ```
     sudo cp /path/to/new/mude.citg.tudelft.nl.pem /etc/ssl/certs/mude_citg_tudelft_nl.pem
     sudo cp /path/to/new/mude.citg.tudelft.nl.key /etc/ssl/private/mude.citg.tudelft.nl.key
     ```

   - Set permissions:
     ```
     sudo chmod 777 /etc/ssl/certs/mude_citg_tudelft_nl.pem
     sudo chmod 600 /etc/ssl/private/mude.citg.tudelft.nl.key
     sudo chown root:root /etc/ssl/certs/mude_citg_tudelft_nl.pem
     sudo chown root:root /etc/ssl/private/mude.citg.tudelft.nl.key
     ```

   - Update nginx configuration:
     ```
     sudo nano /etc/nginx/sites-available/mude
     ```
     Update `ssl_certificate` and `ssl_certificate_key` paths to point to new files. (It will be the same if you follow the instructions)

   - Verify and restart nginx:
     ```
     sudo nginx -t
     sudo systemctl restart nginx
     ```

## Creating New Password for authentication
This process involves a few steps to update your .htpasswd file. Here’s a streamlined guide to help you (there should be better way but this is the only way that I can figure out at this moment, please update this if you find something better!)

1. Create a new password (Delete this file after everything is done.)
Use the following command to generate a new password:
```bash
sudo htpasswd -c /etc/nginx/.htpasswd teacher
#Teacher is the username here.
```

2. Retrieve the New Password\
View the updated .htpasswd file to copy the new password format:
```bash
sudo cat /etc/nginx/.htpasswd
#The format would be this: teacher:$apr1$1ktW7oqwewveq45123dsd
#Teacher is the username and the other is MD5-based Apache crypt (denoted by $apr1$)
```
3. Access the Nginx Docker Container
```bash
sudo docker exec -it website_docker_configuration-nginx-1 /bin/sh
#Replace website_docker_configuration-nginx-1 with your Docker container name if different.
```
4. Create and Edit the Password File\
Inside the container, navigate to /etc/nginx and create a new file:
```bash
cd /etc/nginx
touch $anyname #this name is flexible
vi $anyname
#Press i to enter insert mode
#Paste the copied password format teacher:$apr1$1ktW7oqwewveq45123dsd
#Press Esc to exit insert mode
#Type :wq and press Enter to save and quit
```
5. Create the Configuration File\
Still inside the container, navigate to /etc/nginx/snippets and create a new .conf file:
```bash
cd /etc/nginx/snippets
touch $anyname.conf #this name is flexible
vi $anyname.conf

#Press i to enter insert mode
#Write down folloiwng codes
auth_basic "You shall not pass";
auth_basic_user_file /etc/nginx/$anyname; #this is from step 4
#Press Esc to exit insert mode
#Type :wq and press Enter to save and quit
```

6. Reload Nginx Configuration\
\
Exit the Docker container:
```bash
exit
```

&emsp;&emsp;&emsp;Then reload the Nginx configuration to apply changes:

```bash
sudo docker exec website_docker_configuration-nginx-1 nginx -s reload
```