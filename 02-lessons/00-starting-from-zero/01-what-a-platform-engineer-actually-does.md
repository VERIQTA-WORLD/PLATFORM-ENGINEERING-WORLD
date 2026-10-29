# 00.01 · What a platform engineer actually does

**Start here if you have never worked in technology.** You do not need a cloud account, programming experience or a certification. This lesson takes about 45 minutes. You need only a way to read this page and create a text document.

## Learn the vocabulary through a story

A software application is a program that helps someone do a task. A shopping application might let a customer view products and pay. A developer writes the instructions for that application. A computer executes those instructions. A server is a computer or running program that responds to requests. The word can refer to hardware or software; context matters.

To make an application available to other people, a team must do more than write it. They need a place to run it, a way to configure it, permissions, a way to publish changes, measurements that show whether it works, and a way to recover it. Deployment means placing a chosen version into an environment where it can run. An environment is a place and configuration for running software, such as a laptop or a production service.

Imagine that every developer must ask five people how to do each deployment. One team copies a script, another makes a different copy, and nobody knows which one still works. A platform team builds and maintains a supported route through that repeated work. It might supply a command, a web form, a template, automation and instructions. The platform engineer's task is to make that route useful, safe and maintainable for its users.

This is why we learn both technical mechanisms and user needs. Kubernetes is one possible runtime tool; knowing its commands is not the whole job. A platform can begin with a good script and a clear support contract.

## Follow along: map one request

1. Create a text document named `01-my-first-platform-map.md` in a folder named `99-work`. You can use your file manager; terminal commands come later.
2. Write these five roles: customer, application developer, platform engineer, security owner and service operator. A real person may hold more than one role.
3. Under customer, write “I need to complete a checkout.” Under developer, write “I need to release a corrected checkout service.”
4. Under platform engineer, write “I need to offer a repeatable release path and useful failure feedback.” Under security owner, write “I need the release to respect identity and data boundaries.” Under operator, write “I need to detect and recover a failed service.”
5. Draw arrows in this order: developer requests a release → platform checks the request → runtime starts the application → customer sends a request → telemetry reports the outcome.
6. Circle the user outcome: the customer can successfully complete checkout. Starting a process is one step toward that outcome, not the whole outcome.

## Worked example

A command says “deployment accepted,” but customers still receive errors. The platform has proved that a request was accepted. It has not proved that the application became healthy or produced a correct result. A better platform shows progress, verifies readiness and helps the responsible team diagnose failure.

## Check your understanding

Explain application, server, deployment, environment and platform in your own words. Then answer: who is the user of an internal developer platform? The immediate users are internal engineers completing supported tasks. Their ability to deliver and operate software affects the organization's external users.

## Completion checkpoint

Your document contains five role descriptions, the request sequence and the distinction between accepted work and a successful user outcome. Do not move on if you still think “installing a tool” and “providing a supported platform” mean the same thing.

[Primary reference: CNCF platform terminology](https://tag-app-delivery.cncf.io/wgs/platforms/glossary/).

[Next lesson →](02-set-up-a-computer-for-the-course.md)
