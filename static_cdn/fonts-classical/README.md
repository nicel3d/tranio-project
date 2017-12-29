# Fonts Classical Bower package

A simple bower package, with classic sources. 

Fonts included:

* Arial
* Time New Roman
* Verdana

Package bower created by  [William Canin](http://github.com/williamcanin).

## Requirements for use

| Prerequisite    | How to install 
| --------------- | ------------------------- |
| [NodeJS](http://nodejs.org/)          | **It depends on O.S**     |
| Npm             | **NodeJS contains Npm**     |
| [Bower](http://bower.io/)           | `npm install bower -g`    |

## Using

Navigate to your project's directory and then execute:

```
$ bower install fonts-classical --save
```


## Requirements for developing

| Prerequisite    | How to install 
| --------------- | ------------------------- |
| [Git](http://git-scm.com/)          | **It depends on O.S**     |
| [NodeJS](http://nodejs.org/)          | **It depends on O.S**     |
| Npm             | **NodeJS contains Npm**     |
| [Bower](http://bower.io/)           | `npm install bower -g`    |
| Grunt           | `npm install grunt -g`    |
| Gulp            | `npm install gulp -g`     |

> NOTE: Install the "Grunt" or "Gulp" globally depending on what you use.


You can change the CSS structure using the preprocessor **"LESS"** or **"SASS"**

To do this, perform the following steps:

1) Do the clone and enter the project folder **fonts-classical**.

```
$ git clone https://github.com/williamcanin/fonts-classical.git
$ cd fonts-classical
```

2) Define which preprocessor you use, the Grunt or Gulp running script "init.sh" with command:

```
$ chmod +x init.sh
$ ./init.sh
```

3) Download the dependencies:

```
$ npm install
```

4) Update the 'devDependencies':

```
$ npm update --save-dev
```

5) Make changes to the file "src/css/fonts-classical.css" as you wish.

6) Compile with Grunt:

```
$ grunt
```

7) Compile with Gulp:

```
$ gulp
```

## LICENSE 

[MIT License (MIT)](https://opensource.org/licenses/MIT)
