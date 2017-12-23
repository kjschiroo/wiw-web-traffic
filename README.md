# Web traffic transform #
## Install ##
```
git clone https://github.com/kjschiroo/wiw-web-traffic.git;
cd wiw-web-traffic;
python3 setup.py install;
```
Note: The install process uses `setuptools`. If your machine does not already
have it, install it with `pip install setuptools`.

## Usage ##
```
> wttransform --help
wttransform

Usage:
    wttransform [--verbose] --root_url=<web_log_url> <output_path>
    wttransform (-h | --help)

Options:
    -v, --verbose               Generate verbose output
    --root_url=<web_log_url>    The root url for input csv dataset
    output_path                 The file to write results to
    -h, --help                  Print out this help text
```
### Example ###
An example with verbose output enabled
```
> wttransform -v --root_url=https://s3-us-west-2.amazonaws.com/cauldron-workshop/data/ result.csv
INFO:root:Downloading https://s3-us-west-2.amazonaws.com/cauldron-workshop/data/a.csv
INFO:root:Download complete
INFO:root:Transforming file
INFO:root:Downloading https://s3-us-west-2.amazonaws.com/cauldron-workshop/data/b.csv
INFO:root:Download complete
INFO:root:Transforming file
INFO:root:Reducing datasets
...
INFO:root:Downloading https://s3-us-west-2.amazonaws.com/cauldron-workshop/data/z.csv
INFO:root:Download complete
INFO:root:Transforming file
INFO:root:Reducing datasets
INFO:root:Writing output to result.csv
```

## Assumptions ##
- If there are multiple entries for a user_id path pair, then their lengths should be summed.
- The files under the root url will always be named `a.csv` through `z.csv`. Any other files should not be considered.
