# Webserver Tools and Utilities

# Webserver File System

The webserver hosts websites via `nginx` and the files are located in `/var/web_server/htdocs/`.

# GitLab Runner

GitLab Runner is used to execute the CI/CD (Continuous Integration and Continuous Deployment) jobs defined in a GitLab project's `.gitlab-ci.yml` file. It can be installed on various platforms, including Linux, macOS, Windows, and can also run in Docker containers. In our case, we have GitLab Runner installed on the mude-utilities Linux server.

Currently, most of the mude repositories are using the runner #1020 (rU9Qxsz9J).

### Runner Information

| **System ID**    | **Status** | **Version**           | **IP Address**     | **Executor** | **Arch/Platform**  |
|------------------|------------|-----------------------|--------------------|--------------|-------------------|
| s_1b6e44856200   | Online     | 16.9.1 (782c6ecb)     | 131.180.146.33     | docker       | amd64/linux       |

You can check this information via the [GitLab Runner Dashboard](https://gitlab.tudelft.nl/mude) -> **Build** -> **Runners**.

This runner is located on the `mude-utilities.citg.tudelft.nl` Ubuntu server. To check the status of the runner in the Linux terminal, use the following command:

```sh
sudo systemctl status gitlab-runner
```