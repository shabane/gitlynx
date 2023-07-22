# GitLynx

[GitLynx](https://gitlinks.ir/) is a web app to store your files and get direct link.
you can upload any type of file under 100MB, even you can paste text directly on site and
even it can shorten your URL.



### How it work?

1. FileBin: well it hase a middle server to intract with github.
the middle server runs the site, user will upload its file to the server
and then middle server will save it on github after that it will send back a direct url
of the file to user.

2. PasteBin: this is same as FileBin, execpt that user can write or paste
its text directly on the site and then push it on site to get its URL.

3. Url Shortner: there is a *theme.html* file which contain some html code
and some *URL* varialble, the URL passed from user will store on that variables,
then an **html page** will upload to github which whenever its open, it will
redirect the user to new location.



### Why this Idea!?

In IRAN all **Url Shortner**s, **Pastebin**s and **File Sharing Platform**s are Banned!
so i decide to create a new one which is based on other site that is still open.
if some time Github get banned by Iran, we can replace the github module with anoter module
to save and recive file to/from another site.



### How to deploy our own?

> well its easy with this command

```bash
curl https://raw.githubusercontent.com/shabane/gitlynx/master/install.sh
```

> or you can run and install it manualy

1. clone the repo and set 3 environment varialbes that explained below.

```bash
git clone --depth 1 https://github.com/shabane/gitlynx.git ~/gitlynx
```

|Variable Name|Explain|
|:-----------:|:-----:|
|   TOKEN     | your github token which have access to REPO |
|   REPO      | The repository that you want the site to upload data to |
|   OWNER     | Owner of the repository |

2. install prerequestes

```bash
sudo apt-get update
sudo apt-get install python3-pip
pip3 install requests streamlit
```

3. run site

```bash
nohup streamlit run ~/gitlynx/main.py &
```

### Donation!

Kidding me!? i live in IRAN which get worst every day!
donation **help me** get through!

[Iranian Donation Service](https://daramet.com/shabane)

[Donation with CryptoCurrency](https://shabane.github.io/donate.html)
