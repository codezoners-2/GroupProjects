`-*- mode: markdown; mode: visual-line; mode: adaptive-wrap-prefix; -*-`

# {CODEZONERS} Group Projects

## Introduction

For the remainder of the course, you'll be engaging in small group projects. This process will give you experience in working and contributing as part of a group, and in conceiving and developing your own ideas. We'll be dividing class time between teaching and project time. In terms of "formal" teaching, we have some other topics to cover, but we're also happy to modify bits of the course material to match what you might need for project work - within reason! We don't want to start teaching esoteric topics in support of individual projects, but if there's some common thread or challenge thrown up by several projects, we can look into those.

We want you to program something web-based, which will include a back-end as well as a front-end using the technologies we have seen in the course (although you can go further if you so wish). We’re limiting the scope to web-based works in order to provide more focus, some uniformity and allow you to better include these works in a future portfolio or CV. Naturally, all of the works have to have some kind of interaction with the visitor (this is a coding course, not a web design course), but design is important too...

A significant part of the project work is planning: scoping out the work, delegating tasks to team members, tracking progress, integrating and deploying builds, working to deadlines, and so on. Even though you've been pair-programming for a while, this is your first exposure to collaborating on a shared codebase, and dealing with the issues raised by doing so.

Your code will have to be publicly available on GitHub for all to see - these days, GitHub is an important part of any developer's portfolio - and we’ll show you how to use “git” on your machines so that each of you can work on different parts of the project concurrently without interfering with your other team members, and so that you can merge and integrate everyone's work for testing and deployment.

As a little bonus, bear in mind that you can showcase your work on the 5th of June at the event our guests talked to you about, as well as independently here at Ravensbourne. The Codezoners organizers are really keen for you to produce and showcase what you’ve learned in this course (and so are we!).

## Important Dates and Deliverables

**Monday 13th of April** - On the first day back from holidays, you’ll have to give a 10 minute presentation (with slides!) covering the following topics:

* background research - works you saw that influenced the team’s direction
* your proposal
* a detailed technical specification on the technologies you’re to use. For example, if you are doing data visualization, we’ll want to hear about:
  * the type of data you’re getting
  * the source
  * how you are getting it
  * how you process it
  * what technologies you use for visualization (and why)
  * how you plan to visualize the data (and why)

Expect to answer questions from your peers and us.

Present as a team, rather than as individuals, but each team member should be able to contribute something distinct to the presentation, in support of a specific aspect of the project.

## Architecture

### Back-End (Required)

* Flask server: more documentation [online](http://flask.pocoo.org/docs/0.10/) or by downloading the [book](http://bit.ly/1HKzPos) (ignore security warnings)

* Persistence. We've not yet looked at persisting data between sessions (for example, creating accounts, logging in and out, and so on) - but this is obviously important. We'll be covering this in class; how much detail we go into depends in part on how your projects start to shape up...

### Front-End (One or More Required)

* HTML / CSS
* Bootstrap - [documentation](http://getbootstrap.com/getting-started/)
* P5.js - this can be used either to draw things on the screen, by updating the canvas ([reference](http://p5js.org/reference/) and [examples](http://p5js.org/learn/#examples)) or by updating the DOM elements of a site by using the [p5.dom](http://p5js.org/reference/#/libraries/p5.dom) library - as we did in the [Black Death](https://github.com/codezoners-2/Javascript/tree/master/01_Introduction_to_Javascript/assignments/BlackDeath_P5js_bootstrap/WORKED) assignment. Furthermore, you can also use the [p5.sound](http://p5js.org/reference/#/libraries/p5.sound) library for producing sounds on a site.
* React.js - once more, this could be use in order to dynamically update the DOM without having to reload the page, as demonstrated during the [React.js](https://github.com/codezoners-2/React) week.
* D3.js - a very powerful framework for doing visualizations with Javascript. See [examples](http://d3js.org/). We haven’t seen this yet, but we will work with it soon, so you can still think about where this kind of technology might be used. 

## Project ideas

#### Visualization

* **Text Analysis**: you could use `P5.js`/`React.js`/`D3.js` in order to ask the user for some word and visualize the location of that word in a text. We've already see some of that with frequency. How about something more complex?

* **Statistical Data**: how about loading data from the uk government's [open data](http://data.gov.uk/) initiative and displaying it in an interesting, interactive manner? Alternative sources of data can be found online as well as in the [Data Source](https://quarx.asfa.gr/owncloud/public.php?service=files&t=e7626b4b015023c56f321ab05dbe4cdf) book. [The Guardian](http://www.theguardian.com/data) also has a large set of data sources. (An obvious current topic might be the UK Election in May.) You can see lots of visualization examples in the [D3.js gallery](https://github.com/mbostock/d3/wiki/Gallery).

#### Map Integration

* You could use [leafletjs](http://leafletjs.com/), an easy library for map integration on a site. Maps can be augmented with marker pins, popup windows and so on. Think about:

  * loading data from custom API (implemented yourself and served by Flask)
  * loading data from 3rd party API

* Examples:

  * [Till Nagel](http://tillnagel.com/2013/08/one-year-of-biking/) used his personal biking data to showcase his routes over a year.

  * Another project stripped a submitted Wikipedia article of all the references to cities and towns (by checking if the words existed in a publicly available file of all global towns), then got their locations on earth from a (yet again publicly available) file containing the GPS locations of all towns) and plotted these on a map. This way, one could submit, for example, "Einstein" and see all the places that the wikipedia article mentions in relation to him. The front-end could be a bootstrap page with a form and a map, the user submission is sent to the flask server which strips the wikipedia page and sends back data to be loaded by the javascript-controlled map.

#### Audio

* We haven't discussed the Web Audio API at all yet, but artists are now creating installation works in galleries that have audio processing and mixing served out by web browsers. `P5.js` has an easy library for that - see examples.

#### Image Processing

* Think about using `P5.js` camera functions (and visualizing or sonifying data?).

#### Games

* You might think about various multi-player game scenarios, where the game is mediated by the Flask server, which enforces the game rules and keeps scores and league tables. Obvious (perhaps even cliched) games might be:

  * "Battleships" over the network
  * tik-tak-toe variation (over the network again)

#### A Simple Social Network

* Think about some kind of messaging or bulletin-board system, perhaps integrating image upload, camera image capture and/or sound.

#### Mix and Match

* Some of the best ideas for projects - or startups! - come from taking ideas from seemingly unrelated areas and combining them. Can you think of a game involving maps? What about a messaging system involving sound? Or a social network which can be visualised?
