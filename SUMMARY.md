## Summary

Generally I thought it was a fun exercise. I would like to explore the CLI as well as gain a better understaing of logging and troubleshooting.

### My Approach

1. Review **Getting Started** documentation and Overview of the platform to get an understanding of how things work
2. I forked a simple Flask application
3. Added and update the Dockerfile to build the image
4. I then got a basic GH Action Workflow running on commit
5. I added some simple tests that I could easily force to fail.
6. I then integrated GitHub with the Kubiya platform. (where I currently have 1 remaining issue with triggering the use case)

### Challenges
1. Some how I found multiple version of the documentation, probably googling rather then navigating the Kubiya.ai documentation site. This caused me some issues. It's likely that there are still some publiclly accessable documentation out there that should be rooted out and killed off. :)
2. My development laptop went byby with my recent layoff, I had to recreate my dev environment from scratch before starting, installing all the DevOps tooling that was needed.
3. I had to resist the urge to get too fancy with the tests and documents, as I was on a tight schedule.
4. I do have one remaining issue that the use case isn't triggering on commit to main or completing a pull request. I can interact with AI Teammate within Slack and get the analysis, but I'm not exactly sure why it's not triggering. I did request guidance from support on this after rereading the documentation and regenerating the **Use Case and GH Token**.
