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

This will print out a tab-delimited list of (ip,elapsed) tuples where 'elapsed' is the wall clock time it took for a request to finish. Pipe this output to a file if you wish to do further analysis etc.

# How to mvoe your deployment to a new Region

## Any VM

VMs make it easy to redeploy to a new region through snapshots.

INFO HERE LOL

Finally, start your server back up as you normally would if you turn your server off/on. This will depend on your own configuration.

For example on our python deployment, we run `sudo /opt/bitnami/ctlscript.sh restart apache`.