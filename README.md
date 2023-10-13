# Zultys

## Quick start:

* clone [this](https://github.com/alexc0re/zultys) repo to your local drive

  ```
  git clone git@github.com/alexc0re/zultys.git
  ```
* install dependencies
  ```
  pip install -r requirements.txt
  ```

* Run parametrized download tests
  ```
  pytest -k test_downloads_parametrize
    ```

* Run separately download tests from **test_zultys_downloads.py**
  ```
  pytest -k **test_name
    ```