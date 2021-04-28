---
title: The NAT VPS
date: 2021-02-16
category: hosting
summary: What is a NAT VPS and what makes it so cheap but also, at times, so unreliable? Also find a list of some of the cheapest NAT VPS providers out there.
---


*This article was first published on 2019-10-24.*

Update: This website is now hosted on S3 as detailed [here](https://kenmwanza.org/pelican-s3-route-53-cloudfront.html).

While searching for a home for this website, I came across something I had no idea existed - the NAT VPS.

While I have used other hosting options before, such as regular VPS and shared hosting for my projects, this time I wanted something extremely cheap, since I only needed it to host this site and nothing else.

To my surprise, I found out that VPS price offerings can get to extremely cheap levels. My site (this site) is currently sitting on a 50GB VPS server that costs \$8 a year!

As someone who has only used options that go from \$6 to \$10 a month, this was an eye opener.

So what are these VPS hosting plans that are priced so low? Welcome to the NAT VPS world, where you can get a VPS for \$4 a year.

## What is a Virtual Private Server (VPS)?
So here's a quick primer for those unfamiliar with the term.

A VPS is a [virtual machine](https://en.wikipedia.org/wiki/Virtual_machine) offered as a service. There is a multitude of providers of VPS services that can be found with a quick Google search ([Linode](https://linode.com) and [Vultr](https://vultr.com) are my favourite.)

## What is a NAT VPS?

![How a NAT VPS works]({static}/images/nat vps.png)

Simply put, a NAT VPS is a VPS that uses a shared IP address, as opposed to a dedicated IP which ordinary VPSs use.

### What is NAT?

NAT stands for network address translation, which is simply a process in which routers map internal IP addresses in an organization  to an external (public) IP address which then links them to the Internet.

In this regard, a NAT VPS is a VPS which shares a public IP address with other VPSs in the same pool.

With this definition, we can already see a pro and con of the NAT VPS. The obvious benefit is the low cost of the NAT VPS due to them not having a dedicated public IP. On average, a dedicated IPv4 address costs around \$1 - \$2/month. Sharing this IP with others slushes the cost down significantly.

The obvious flaw of the NAT VPS is increased security risk, since you're sharing the public IP with other users. For example if one of the users you share your IPv4 address with gets a DDoS attack for whatever reason, everyone in the pool will get affected.

### Features of the NAT VPS

1. They can be extremely cheap (some go for as low as $3/year)
1. They use shared IP addresses
	1. Each user typically has a redirect port to ssh into the server with the given shared IP Example SSH command: `ssh root@192.xx.xx.xx -p xxxx`

1. Most providers offer extremely poor technical support (unmanaged services) - additional technical support is offered at a (relatively) steep cost
1. NAT VPSs are mostly ultra low spec (I've encountered some with as low as 128MB of RAM, 3GB storage and 128GB bandwidth)

### Why I host my website on a NAT VPS
So despite the downsides of the NAT VPS, why am I hosting this website on one?
Well, for me, this is just an experiment. It's a new thing that I discovered and just want to see how far I can take it before its limitations start to creep up.
Plus, this is not a very critical website anyway, and, in case of security issues, I can always move it to a dedicated IP VPS.

### When to use a NAT VPS
NAT VPS are mostly suited for fun little projects. 
A few ideas for projects that use NAT VPSs come to mind:

1. To host personal websites
1. To host VPN servers
1. As Minecraft servers
1. As seedboxes
1. As Discord servers
1. To host [Nebula](https://github.com/slackhq/nebula)

### When not to use a NAT VPS
By no means should a NAT VPS be used for mission critical applications.

Do not use a NAT VPS if your technical knowledge is minimal (and/or are not willing to take the time to learn how to use them). As earier stated, technical support for these servers is limited if not non-existent.

If you can't stand constant interruptions due to frequent server downtime, do not use this type of server.

Do not use if you are unwilling to accept security risks that are brought on by sharing IP addresses with other (unknown) users.

If you would want to initiate a chargeback after getting poor service, please don't bother with this type of server as many providers do not allow chargeback claims in case of a dispute. And if you go ahead and file a chargeback, many will straight up delete your account.

So if after reading this you've decided that NAT VPSs are beyond you, do not be discouraged as ordinary (read managed) VPS providers are still available at Vultr, Linode or Digital Ocean. Otherwise, forge ahead! An adventurous  journey awaits you.

### Some NAT VPS providers

To get you started, here is a list of some cheap NAT VPS providers:

| Provider           | Location                                                | RAM   | Storage | Virtualization | Price Per Month |
|--------------------|---------------------------------------------------------|-------|---------|----------------|-----------------|
| [Gullo Hosting](https://hosting.gullo.me/order/main/packages/bundles/?group_id=33)      | Chicago, Buffalo, Canada, Germany, Finland and Bulgaria | 128MB | 3GB     | OpenVZ         | $1              |
| [Signal Transmitter](https://signaltransmitter.de/ssd-lxc-vserver) | Germany                                                 | 512MB | 10GB    | vServer        | €2.99           |
| [RackNerd](https://my.racknerd.com/cart.php?a=view)           | Los Angeles                                             | 512MB | 30GB    | KVM/SolusVM    | $1.92           |
| [BuyVM](https://buyvm.net/kvm-dedicated-server-slices/)              | Las Vegas, New York and Luxembourg                      | 512MB | 10GB    | KVM            | $2.00           |
| [Strato](https://www.strato.de/server/linux-vserver/mini-vserver/)            | Germany                                                 | 512MB | 10GB    | vServer        | €1              |

[Here](https://www.lowendtalk.com/discussion/153227/let-provider-register-directory-find-your-next-host-here/p1) are a few more NAT VPS providers from the LowEndTalk forum that I have come across.

Please note that is not a definitive list of NAT VPSs and it's important to do your own research and due diligence before purchasing VPS hosting services.
