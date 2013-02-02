WebpageLinkParser
=================

Small project for parsing tags inside links. Desgined to be used at ```www.vg.no``` and ```www.nettavisen.no```, but will be expanded so it can handle anything thrown at it.


## Usage

`settings.json`
The `settings.json` file is where you decide upon the websites to parse, and what domain too include. 
* `[main domain]` is the site you are suppose to parse. 
* `[domain]` && `[another domain]` is the websites we are whitelisting to have tags from.
More websites can be added too the json and accepted. 
```
{
    "www.[main domain].com": [
        "www.[domain].com",
        "www.[another domain].com"]
}
```
When settings are set, run `run.py`. The script will be running through the directories too look for directories with the same name as the website in the settings. If there is, you will be asked if you want too search the dir after htm/html files too find tags. If not, it will go to the website and parse the tags.

## Output
In the `output` folder we will have the results of the search. The output the tags and how many it found, sorted into json (another format will be added).

	{
	    "www.[main domain].com": {
	        "/news/war": 14,
	        "/news/celebreties": 20
	    }
	}

Inside the `tmp` folder we will have two files, one containing ALL parsed links (read whitelisted and parsed), and one which contains all files we have parsed before.