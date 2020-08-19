# retardify-commits

*Entry to the DEV.to Github actions contest - Wacky wildcards category*

Having conventional, easy-to-read and meaningful commit messages is boring. **Having wacky, Spongebob memesque commit messages is fun!**

Basically it transforms your commit messages to retarded-case. What is retarded-case? It's this:

![](https://github.com/andraspatka/retardify-commits/blob/master/spongebob.jpg)

## Support for conventional commit messages!

Using [conventional commit messages](https://www.conventionalcommits.org/en/v1.0.0-beta.2/) makes the commits more readable and communicates the author's intent in a really straight-forward way. In other words: It's for nerds. That's why if this github action detects any type of conventional commit message, it replaces the "tag" with the following message: "i am a smartass" (please note that this too will be transformed to retarded-case. No message is safe!)

## How to use

**Please don't use this.**

I purposefully did not publish this to the Github Actions Marketplace. I don't want to encourage anyone to use this abomination.

If you **really really** want to use this, then just copy the following scripts to your repo:
 - asciiArt.py (fancy, isn't it?)
 - retardify.py (ThiS iS whERE thE MAGiC HapPens)
 - .github/workflows/retardifier.yaml (workflow file)

You must also create two secrets:
 - EMAIL: Email address used for git
 - FULL_NAME: Full name for the commit message

I recommend that you use a fake email address and full_name, so that no one can link these wacky commit messages back to you! :)
