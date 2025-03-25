# GITLAB Pipeline

# GitLab CI/CD

Note that the TU Delft GitLab (`gitlab.tudelft.nl`) has a limited set of features compared to EWI GitLab (`gitlab.ewi.tudelft.nl`).  

There is a different setup on the `mude` and `interactivetextbooks` servers.

Here is the explanation for example `https://mude.citg.tudelft.nl/archive`

## GitLab CI/CD Pipeline Configuration

This configuration defines a CI/CD pipeline that deploys files to an archive directory on a remote server. The pipeline uses the latest Alpine Linux image and includes the following key sections:

### Stages

```yaml
stages:
  - deploy
```

- Stages: Currently, only a deploy stage is defined. Typically, pipelines include test, build, and deploy stages.
Rules: The job triggers only on pushes to the main branch

```yaml
deploy-to-archive:
  stage: deploy 
  #this part should be the same as the pre-defined ones.
  rules:
    - if: $CI_COMMIT_BRANCH == "main" && $CI_PIPELINE_SOURCE == "push"
```

- Rules: The job is triggered only when a push is made to the main branch.

```yaml
before_script:
  - apk update && apk add --no-cache rsync openssh
  - eval $(ssh-agent -s)
  - echo "$MUDE_DEPLOYER_SSH_KEY" | tr -d '\r' | ssh-add -
  - mkdir -p ~/.ssh
  - chmod 700 ~/.ssh
  - echo -e "Host *\n\tStrictHostKeyChecking no\n\n" > ~/.ssh/config
```
- Install Dependencies: Updates package list and installs rsync and openssh.
- SSH Setup: Initializes SSH agent, adds SSH key, and configures SSH to skip host key checking.

```yaml
script:
  - 'echo "Current directory: $PWD"'
  - ls -la
  - if [ ! -d "src" ]; then echo "src directory does not exist. Creating it..."; mkdir src; echo "Moving necessary files to src directory..."; mv *.html *.js *.css src/ 2>/dev/null || true; fi
  - echo "Contents of src directory:"
  - ls -la src
  - rsync -avz --delete-after --exclude=".git/" --exclude=".cache/" --exclude="venv/" src/ $MUDE_SERVER_USER@$MUDE_SERVER_ADDRESS:/tmp/archive_update/
  - |
    ssh $MUDE_SERVER_USER@$MUDE_SERVER_ADDRESS "
      sudo rsync -avz --delete-after /tmp/archive_update/ /var/web_server/htdocs/archive/ &&
      sudo chown -R root:root /var/web_server/htdocs/archive &&
      sudo rm -rf /tmp/archive_update &&
      sudo chmod 755 /var/web_server/htdocs/archive
    "
```
- Debug Information: Displays current directory and lists files.
- Directory Preparation: Checks for src directory, creates it if missing, and moves necessary files into it.
File Syncing: Uses rsync to sync files to a temporary directory on the remote server.
- Remote Commands: Executes SSH commands to update the archive directory on the remote server:
Syncs files to the target directory.
Changes ownership and permissions.
Cleans up temporary files.

```yaml
environment:
  name: production
  url: https://mude.citg.tudelft.nl/archive
```
- Environment URL: Specifies the URL for the production environment.

Basically, this configuration ensures that only changes pushed to the main branch trigger the deployment, securely transfers files, and updates the remote server's archive directory.

This pipeline can be used for other server setup as well, but you need to define the CI/CD variables first.

## Setting Up CI/CD Variables
Navigate to your repository -> Settings -> CI/CD -> Variables
Define these variables:

1. MUDE_SERVER_ADDRESS: Current value = mude.citg.tudelft.nl
2. MUDE_SERVER_USER: Current value = kwangjinlee
3. MUDE_DEPLOYER_SSH_KEY: SSH private key for authentication
   - This is already done for `mude.citg.tudelft.nl`
   - First of all, create a ssh key using the following ssh-keygen command
      ```sh
      ssh-keygen -t rsa -b 4096
      ```
   - When you run this command:
      - It will prompt you to choose a file location to save the key
      - You'll have the option to set a passphrase (recommended for security)
   - This generates two files:
      - A private key (e.g., id_rsa)
          - Define this as the MUDE_DEPLOYER_SSH_KEY CI/CD variable
      - A public key (e.g., id_rsa.pub)
          - Add this to ~/.ssh/authorized_keys on the server

This process enables SSH connection without specifying a key.

## Recommendations for Future Development
- Update the MUDE_SERVER_USER to ensure an authorized username is used.
- Consider adding additional stages (e.g., test, build) to the pipeline for a more comprehensive CI/CD process.
- Regularly review and update the SSH keys and server access permissions for security.