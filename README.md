# lark-space-alfred-workflow

An Alfred workflow to search Lark Space with instant results.

Based on notion-search-alfred-workflow, thanks.

Simply type your keyword into Alfred (default: lk) to see instant search results from Lark Docs. Selecting a search result takes you to that page in Lark Docs in your default web browser.

## Installation


## Feature

### 1. Search docs

type `lk [doc_name_you_want_to_search]` in Alfred, you will see results coming in if there are matches.

![](https://i.loli.net/2020/08/14/Gx8PQftEpA3WCgF.png)

### 2. Create new Lark Doc

type `lkc` in Alfred to trigger a file type filter, confirm to create a new Docs or Sheets.

![](https://raw.githubusercontent.com/hikerpig/lark-space-alfred-workflow/master/screenshots/create-doc.png)

## Setup

### 1. Get your Lark Domain

Normally it's something like `https://*.larksuite.com` .

### 2. Get cookie session

Goto any Lark Docs page in your browser, make sure you are logged in. Then:

open Devtools -> Application -> Cookies -> check your lark domain's cookies -> copy the value of `session`

![](https://i.loli.net/2020/08/13/c7eyYaC2quAiOKS.png)

### Set variables in Alfred workflow

Paste those two variables into workflow configuration.

![](https://i.loli.net/2020/08/14/huFpDeo2xNLsRqi.png)

And there are other variables:

- `pythonPath`, path to python 2 executable, for example: `/Users/hikerpig/.pyenv/versions/2.7.18/bin/python`
