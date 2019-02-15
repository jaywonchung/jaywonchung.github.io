---
title: "[Review] Modern Javascript Explained for Dinosours"
excerpt: "Medium, Oct 19, 2017. How did modern javascript evolve? What were their motivations of evolving?"
categories:
  - read
  - articles
---
## Article
[Modern Javascript Explained for Dinosours (Medium, Peter Jang, Oct 19, 2017)](https://medium.com/the-node-js-collection/modern-javascript-explained-for-dinosaurs-f695e9747b70)

## Summary
This article briefly summarizes how technologies related to JavaScript evolved, which was a cogent flow of increasing productivity and solving the vices of existing technology.

Following the chronology, we begin with old-school HTML and JavaScript. When we want to include an external library, we use the following code.

```HTML
<script src="moment.min.js"></script>
```

This code is easy to read, but we need to download the ```moment.min.js``` file every time it updates and manually include it.

To ease this pain, the JavaScript package manager was introduced. Currently the most popular one is npm. Npm automatically downloads the most recent library file to the project ```node_modules``` folder, easing the user of the tedious effort of finding and downloading each code file. Also, it creates a ```package.json``` file with a list of dependencies and their versions, making it easy for developers to share the environment in which the code was created. However, still, the user has to manually include the source code with the ```<script>``` tag, which now is located deeper inside the ```node_modules``` folder.

Node.js made the process of including much easier by introducing the ```request()``` function. The following JavaScript code can be used to include the library.

```javascript
var moment = require('moment');
```

However, node.js is a server-side technology as opposed to JavaScript, which is a client-side technology. Thus, the browser which interprets the JavaScript code does not have access to the file system, giving an error when encountering the ```request()``` function. For this, the JavaScript module bundler was created in an attempt to specify an ecosystem for JavaScript outside the browser. The most popular of this kind is webpack. As an extension of npm, webpack builds the target ```index.js``` file to create a final output ```bundle.js``` compatible with the browser. Now the developer can include the ```bundle.js``` file to ```index.html```, and the browser works as planned.

A downside of this is that we need to run the webpack command every time we change the JavaScript file. To automate this process, ```packages.json``` can be used for implementing advanced features. By adding values in the "script" key, we can use the task runner in the npm.

1. "build": Control action during the build, such as minimizing code.
2. "watch": Rerun webpack whenever any JavaScript file changes.
3. "server": Open the ```index.html``` in the browser and refresh it whenever any JavaScript file changes.

Also, webpack has a configuration file ```webpack.config.js```, where you can add rules for building the file. If you want to transpile some code that includes new JavaScript features (liks ES2015 and beyond) so that it's compatible with older browsers, you can intall Babel and add it to the build rule.