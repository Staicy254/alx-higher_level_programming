# Working with JSON Data

This guide provides an overview of working with JSON data in a modern JavaScript environment. It covers accessing attributes of a JSON object, utilizing the `request` module, and adhering to best practices in contemporary JavaScript development.

## Overview

This project demonstrates the workflow of accessing attributes from a JSON object created by Jimmy Tran from Cohort 1 - San Francisco. The guide will walk you through creating a simple JSON object, accessing its attributes, and making HTTP requests to fetch JSON data using the `request` module.

## Prerequisites

To follow this guide, ensure you have the following installed on your system:
- Node.js
- npm (Node Package Manager)

## Setup

1. **Initialize a new Node.js project:**

    ```bash
    mkdir json-workflow
    cd json-workflow
    npm init -y
    ```

2. **Install the `request` module:**

    ```bash
    npm install request
    ```

## Creating and Accessing JSON Data

### Step 1: Create a Simple JSON Object

Create a JavaScript file named `index.js` and include the following JSON object:

```js
const jsonObject = {
    "name": "Jimmy Tran",
    "cohort": "Cohort 1 - San Francisco",
    "skills": ["JavaScript", "Node.js", "React"]
};
```

### Step 2: Access JSON Attributes

Access the attributes of the JSON object:

```js
console.log(`Name: ${jsonObject.name}`);
console.log(`Cohort: ${jsonObject.cohort}`);
console.log(`Skills: ${jsonObject.skills.join(', ')}`);
```

### Step 3: Fetching JSON Data with `request` Module

Use the `request` module to make HTTP requests and fetch JSON data. First, import the `request` module:

```js
const request = require('request');
```

Make a GET request to fetch JSON data from a URL:

```js
const url = 'https://api.example.com/data';

request(url, { json: true }, (err, res, body) => {
    if (err) {
        return console.error(err);
    }
    console.log(body);
    console.log(`Attribute: ${body.attributeName}`);
});
```

## Running the Code

Run your `index.js` file using Node.js:

```bash
node index.js
```

You should see the output of the accessed attributes from the JSON object and the fetched data from the HTTP request.

## Conclusion

This guide has covered the basics of working with JSON data in modern JavaScript. You have learned how to create and access a JSON object, as well as how to fetch JSON data using the `request` module. This workflow is fundamental for handling JSON data in various JavaScript applications.


