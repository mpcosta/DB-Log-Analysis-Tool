# Database Log Analysis Tool

Source code for an internal reporting tool that outputs important data about a news website databse.

## Features

- Ability to output the (X) Most Popular Articles of all time;
- Ability to output the Most Popular Authores of all time;
- Ability to present the Date in which more than (X) Requests to the website led to errors.

## Code

In order to run this code, please set up a [Vagrant](https://www.vagrantup.com/) environment supplied by the following [Configured Linux Virtual Machine](https://d17h27t6h515a5.cloudfront.net/topher/2017/August/59822701_fsnd-virtual-machine/fsnd-virtual-machine.zip).  
After this process, clone this repository into the Vagrant environment location.

Once inside this location start up the Virtual Machine with `vagrant up`.
This will cause Vagrant to download the Linux operating system and install it.
When `vagrant up` is finished running, you can then run `vagrant ssh` to login in into the Linux VM.

After this process please download the [news data](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip), unzip the `newsdata.sql` and put this file in the same Vagrant directory.
Run `psql -d news -f newsdata.sql`.

Final process you just have to run `python news_log.py` in order to get the results from the log tool.

Inside the `news_log.py` you can change parameter values of some methods inside the main class in order to obtain different results.
Example:
```python
# Will get the 4 most popular articles
get_most_popular_artc(4);

# Will get the day with error requests above 2%
get_most_err_req(2);
```

## Interface

Shell Based Interface with the requested results.  


![img](http://i.imgur.com/Flr4P7H.png)

