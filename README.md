# IP Timing

Test timing for GCP deploy regions. This project requires pyyaml, which we include in our Pipfile.

Run `pipenv install` to install the virtual environment. Run `pipenv shell` to enter it.

Run the code with `python timing.py [filename]` where `[filename]` is a .yaml file of the format:

```
---
  ips:
    - IP_ONE
    - IP_TWO
    - IP_N
```

For an arbitrary number N of IPs.

# How to move your deployment to a new Region

## Any VM (Python or Java)

VMs make it easy to redeploy to a new region through snapshots.

Go to your VM instances. On the sidebar, look for the "Snapshots" menu item.

![snapshots](pics/sidebar_snapshots.png)

On the top bar, click the 'Create Snapshot' button.

![create snapshot](pics/snapshots.png)

Name the snapshot anything you'd like, and select a region in which to save it. This does NOT have to be the region you want to redeploy to - this is all just storing some data somewhere.

The most important thing is to select the VM you want to redeploy in the "Source disk" combo box.

![sksksks](pics/creating.png)

Wait for GCP to take a snapshot of the disk. Once it does, it will appear on the Snapshots page. Once it does, click its name.

On the details page, click "Create Instance." This will create an instance from the snapshot. Deploy as you would a normal instance, being sure to select the correct region where prompted.

![do it](pics/createit.png)

Finally, start your server back up as you normally would if you stop/start your instance. How this is done will depend on your own configuration. For example, on our python deployment we run `sudo /opt/bitnami/ctlscript.sh restart apache`. You can choose to configure your system such that these commands are run on boot, making the transition seamless. 