# ezeahunanya
This project contains the source code files for my personal blog. I used
pelican to create the html files for the webpages.

To view my blog please visit <ezeahunanya.com> or <ezeahunanya.github.io>.

## Installation

To run create the output files used for my website python needs to be installed.
Pelican and markdown also needs to be installed. Anaconda will install python.

Anaconda is available for Windows, Mac OS X, and Linux. You can find the installers at https://www.anaconda.com/download/ and the installation instructions [here](https://docs.anaconda.com/anaconda/install/).
Once Anaconda is installed update all the packages. This can be done by running the following code in the Anaconda Prompt:

```
conda upgrade --all
```

Then pelican and markdown can be installed by following the instructions [here](https://docs.getpelican.com/en/3.6.3/quickstart.html).

Clone the GitHub repository by running the following code in command line:

```
git clone https://github.com/ezeahunanya/ezeahunanya.git
```

To create the static files for my website run the code in command line:

```
pelican content -s pelicanconf.py
```
