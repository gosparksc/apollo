# Apollo
The Repository for Apollo, USC's first innovative journalism platform. Run by students that care.

***Jekyll***

Apollo is built on the jekyll. Jekyll is a static site generator that makes it easy to convert plain text files into styled web-pages, and was specifcally designed with blogs in mind. Static site generators look at files in a project repository and use the information in these files, as well as inputs from the user (developers), to prorammatically generate the desired HTML/CSS/JS files. Jekyll and other static site generators expect certain directory structures and files to be provided by the developer. All files and directories beginning with an underscore ('_') in this project are recognized by jekyll, and are used to help jekyll figure out how to construct the finalized html/css/js package. <code> jekyll build </code> will start this process, and will output the final package (the files that should be hosted on the live server) to the _site folder. For development, <code>jekyll serve</code> will serve the output files locally.

***Folders***

_includes contains html snippets that may be shared/consistant across multiple portions of the website (e.i. headers and footers).

_layout defines the general structure of the blog's main types of pages: the default, the posts, and the general, non-post pages.

_site is the folder that jekyll output to compiled HTML/CSS/JS files to, and the files in this folder are what should be hosted on the server.

_posts contains markdown files that contain the meta data and text content for each post. On build, jekyll generates HTML files for each of these posts. In the posts we specify the "category" that the post belongs to, and jekyll uses the information to determine the directory that the post ends up in in _site, and ultimately help jekyll determine the url of the post's html page.  

_pages contains the different general pages of the site.

_plugins

_includes

***Front Matter***


***Using Stylus***

Stylus allows us to write more readable and effective styling for html pages. Ultimately, .styl files get compiled down to .css files, but make development more effective and fun! The stylus plugin used here transforms any .styl file to a .css file with the same location in the directory structure in the output directory. All style files need to have empty Front Matter.


TODO for README.md:
- Link to jeckyll docs in different places.
- Link to Stylus docs.
- Breifly Explain Front Matter.
- Expand on folders section.
- Breifly Explain CNAME.
- Breifly Explain Gemfile

General TODOS:
- Test making pages
- Integrate Joseph's index.html