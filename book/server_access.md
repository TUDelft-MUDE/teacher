# Server Access

# Accessing the server

Once you have been granted access to a server, the email instructions from ICT are sufficient if you have experience with ssh. The DCC has a [page explaining how to access servers](https://tu-delft-dcc.github.io/infrastructure/VPS_SSH.html) as well. If you don't want to use the terminal, use WinSCP; this is a GUI that makes it very easy to inspect, edit and transfer files on the webserver.

_These instructions were tested with an existing `id_ed25519` key, assume you already have WinSCP installed and can modify a text file on the server in your user directory using the terminal._

1. log in to the server and add your public key to the file `/home/rlanzafame/.ssh/authorized_keys`

It should look like this with your own keys `XXXXXXX` and NetID filled between the `<...>` (note the `<XXXXXXX>` is much longer in reality):
```
ssh-rsa <XXXXXXX> ICT-SYSTEMS-<NETID>
ssh-rsa <XXXXXXX> ICT-SYSTEMS-<NETID>
ssh-ed25519 <XXXXXXX> <NETID>@tudelft.nl
```

2. Using WinSCP, the following fields should be entered:

On the main login settings page:
- File protocol: `SFTP`
- Host name: `<server>.citg.tudelft.nl`
- User name: your NetID

3. Open the "Advanced..." window

4. On the page "Tunnel" (under heading "Connection," still in the Advanced window):
- Host name: `linux-bastion-ex.tudelft.nl`
- User name: your NetID

5. On the page "Authentication" (under heading "SSH," still in the Advanced window):
- Private key file: select your private key file, for example `C:..../<username>/.ssh/id_ed25519`
- Note that the app may ask you to convert your existing key to a Putty format (for example "Do you want to convert OpenSSH private key to PuTTY format?"). Click "OK" then make sure you select the new PuTTY file (e.g., `C:..../<username>/.ssh/id_ed25519.ppk`)

6. Save the setting and click "Login", using your NetID password to authenticate.)

## Using WinSCP with sudo rights

If you have sudo rights on the webserver you can use this via WinSCP as follows:
1. Once agin go to the "Advanced..." window to the "SFTP" page under heading "Environment"
2. In field "SFTP server" enter the following: `sudo /usr/lib/openssh/sftp-server`
3. Save the changes
4. Use with caution!

Note that the path to `sftp-server` may be different but can be easily checked and arranged. This will not work if you change the setting and continue to use an open session.

## Server Request

Servers can be requested via the service desk. See an old ticket and duplicate the standard setup. Note that sometimes there are issues in the firewall being set up properly (this seems to be done by a separate sub-group within ICT).

To gain access to an existing server (request sudo rights), you will need permission of the staff member that is responsible for the server (ICT keeps track of this). You can submit the request, but this person needs to approve (or submit) it. Something like this usually works: _"Hello, please give access to PERSON with netid NETID to server SERVER."_

Upon gaining access to a server, you usually recieve an email with the following instructions (user and server varialbes generalized using brackets, `<...>`).

```
===
Title: New Server <server_name>.citg.tudelft.nl is ready - callnr <XXXXXXXXXX>
Sender: sysadmin@ict-sys.tudelft.nl.
===

Hi <name_of_user>,

Server <server_name>.citg.tudelft.nl is successfully deployed.

To follow the login procedure:
From your laptop/pc -> linux-bastion-ex.tudelft.nl -> <server_name>.citg.tudelft.nl

  - Step A: use <netid> NetID login credentials to authenticate
  -->   ssh <netid>@linux-bastion-ex.tudelft.nl
then:
  - Step B: use SSH Key-Based Authentication
  -->   ssh <server_name>.citg.tudelft.nl

On question:
  Are you sure you want to continue connecting (yes/no)?
Answer: yes


You can connect and log-in with your NetID.

Your login details are as follows:
      Username: <netid>
    Servername: <server_name>.citg.tudelft.nl
  Extra option: sudo privileges

Beware: you must use the fully qualified domain name (FQDN). Example:

[<netid>@<server_number> ~]$ ssh <server_name>.citg.tudelft.nl

It may be that the network or firewall change have not yet been activated.
(this may take a few days).

====
More information:
  https://www.tudelft.nl/ict-handleidingen/linux-bastion-host/
  and click on the link "Remote Connection".
====

Kind regards,
Sysadmin

ICT-SYSTEMS-SERVERS-LINUX
```
