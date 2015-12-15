# A minimal Python Github API

##Why this API?

This extremely minimal python api wraps the github api in the way that makes the most sense - by doing almost none of the work.

Instead of trying to wrap every possible case and then write documentation for all of these wrapped calls I simply generate the wrapper in it's current form.  If you want to know how to use my client I'd refer you to the [github api curl documentation](https://developer.github.com/v3/).

The big problem in the past for writing a github client for python has been it doesn't have official support from github.  So rather than trying to fight to make this unofficial api as good.  Why not simply take advantage of the great work github is already doing?  

This api is not as intuitive as it could be.  But without full funding, no python api ever will be.  Since github is mostly a ruby / javascript shop, this is unlikely going to be the case in the near future.

So, in the meantime, this is my solution.  

#Some prerequiste knowledge

This api assumes you are using 2 factor authentication.  If you aren't please use [PyGithub](https://github.com/PyGithub/PyGithub), it's really really good, except for it's lack of support for 2 factor auth.  

If you are using 2 factor authentication (on your github account) this is the api wrapper for you!

First you'll need to [generate your authentication token](https://help.github.com/articles/creating-an-access-token-for-command-line-use/)

Remember to give it all the access you want to be able to use from this api.  If you don't click a checkbox when you are generating the token and then want to use that endpoint, you'll need to create a new token with that access right.

Please save your authnetication token in a file called `oauthkey.pickle` - the ability to save to whatever file you want will be available in future releases of the tool.

#How to use

This api is extremely simple to use:

Look up the api call you want to make from the [github api curl documentation](https://developer.github.com/v3/).  Then you simply need to designate a .json file to save this to.  From there you'll be passed back a dictionary which you can interact with as you please!  

###Making a request
```
from client import make_request
response = make_request(
        endpoint="https://api.github.com/orgs/hackingagainstslavery/members",
        output_file="members.json",
        parameters = {
            "per_page":"200"
        })
    
```

Note the parameters dictionary takes in any parameters you want.  At this time I don't check to see if the parameter will actually work for the given endpoint so you'll need to make sure you are passing the appropriate parameters yourself.

Note that make_request will generate a persistent json file with the name of `output_file`.  If you'd like this to not happen, you can turn persistance off with the following call, instead:

```
from client import make_request
response = make_request(
        endpoint="https://api.github.com/orgs/hackingagainstslavery/members",
        output_file="members.json",
        parameters = {
            "per_page":"200"
        }
        persistent=False)
    
```


    
