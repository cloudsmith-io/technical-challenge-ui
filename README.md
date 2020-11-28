# Technical Challenge - UI Skeleton

## What Dis?

This is a base/empty skeleton UI project, used for Cloudsmith technical challenges. Candidates can use this as the base for an UI-based solution, or they can forego that and use their own. The choice is yours. >:)

For instructions on what to do (plus using this repository), please refer to the challenge document.

## Prerequisites

This is a challenge best completed on Linux, but running on MacOS and within WSL2 on Windows works too.

The only thing you *need* to install is:

- [Docker](https://www.docker.com)
- [docker-compose](https://docs.docker.com/compose/install/)

The following utilities might help for testing purposes:

- `curl`

## Setup

First you need to prime the database. This is a one-time thing, unless you make schema changes.

Run the following commands, in one window / pane:

```bash
docker-compose build
```

```bash
docker-compose up
```

Then run these in another window / pane (while keeping `up` running):

```bash
docker-compose exec web challenge db upgrade
docker-compose exec web challenge init
```

This will (1) build the container, (2) setup the sqlite database, and (3) create an admin user.

Note: You can avoid having to run in the background by using `docker-compose up -d`.

## Running

Once you're setup as above, you can run anytime using:

```bash
docker-compose up
```

You'll now be able to connect to http://localhost:5000 to reach the API.

Try the root page to see if it works (or visit it in a browser for more impressive visuals):

```bash
curl -1slf http://localhost:5000/ | head -n5
```

The output should look like this:

```html
<!DOCTYPE html>
<!-- Welcome to The Challenge -->
<html class="no-js" lang="en">
  <head>
```

So if you get that response, it's working. \o/ Now go forth, and create!

## Assets

Webpack is used to build the assets, and this is done both statically (at
build time, into the container), and dynamically. So you can make changes
to anything in the `assets` folder, and they should be reflected quickly
after the rebuild. Without any further action necessary on your part.

## Testing

If testing is your thing, then you've got tests available.

You can execute the tests by running:

```bash
docker-compose run -v $(pwd)/tests:/code/tests:ro web tox -e test
```

You can also run *just* the linting (checks formatting):

```bash
docker-compose run web tox -e lint
```

## Where to Edit

Short answer: Wherever is required. :-)

Slightly more helpful answer:

 - `challenge/views.py` - Where you'll create new views (code for "pages").
 - `challenge/templates/*` - Where you'll create new templates (rendering for "pages").
 - `challenge/models.py` - Where you'll create new (data) models, if you need them.

Anything else is optional and at your perogative!

Remember: Things are missing on purpose. If you don't know what, you might not need it. Focus
on the task at hand. If you've got spare time at the end, *only then* do optional extras.

## Finally ...

Good luck + have fun!
