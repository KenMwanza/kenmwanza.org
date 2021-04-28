---
Title: How to Resolve the Permission denied (publickey) Error in Bitnami Lightsail
Date: 2021-03-2
Slug: lightsail-bitnami-permission-denied-publickey
Category: hosting
Summary: A step by step guide on how to resolve the "Permission denied (publickey)" error when trying to ssh into a Bitnami Lightsail instance.
---

## Introduction
**Please note that this post involves enabling password authentication and changing your public key in the `/home/bitnami/.ssh/authorized_keys` file.**

I needed to ssh into my Amazon Lightsail instance but kept getting a "Permission denied (publickey)." error as shown below:

![Permission denied (pinlickey)]({static}/images/error-permission-denied.JPG)

Connecting through the browser-based SSH client also did not help because I got a "CLIENT_UNAUTHORIZED[769]" error as shown below:

![CLIENT_UNAUTHORIZED [769] error on browser-based ssh client lightsail]({static}/images/browser-ssh-client-unauthorized-error.JPG)

I figured that I may have messed up something on the instance's SSH settings (specifically the `authorized_keys` file. After googling for solutions to no avail, here is what I did to resolve the problem.

### Requirements

You will need an SSH key pair. You can generate one from a private key using something like [PuTTYgen](https://puttygen.com) or OpenSSL. To get the default private key, go to the **Account** > **SSH Keys** tab. If you have already generated a key pair, you can upload your private key here.

## Solution

I created a new instance from **Snapshots** (If you do not have automatic snapshots enabled, you will need to create a manual snapshot under the **Snapshots** tab of your instance).

### Steps

(1) Click on **Create new instance** on the right side of your instance snapshot:

![Create new instance from Snaphsot]({static}/images/step-1-create-new-instance-from-snapshot.png)

(2) On the next page, we will need to add a `Launch script` to run when the instance is initialized. So click on the `Add launch script` link to reveal a text area in which to add our script.

![Create new instance from Snaphsot]({static}/images/add-launch-script-link.png)

This script will
    
   1. enable password authentication on the `/etc/ssh/sshd_config` file,
   2. delete everything on the `/home/bitnami/.ssh/authorized_keys` file,
   3. add a new public key to the ``/home/bitnami/.ssh/authorized_keys`` file,
   4. create a password for user `bitnami` and,
   5. restart sshd process.
  
#### The Launch script

    :::bash
    
    sed -i "/^[^#]*PasswordAuthentication[[:space:]]no/c\PasswordAuthentication yes" /etc/ssh/sshd_config
    > /home/bitnami/.ssh/authorized_keys
    echo -n "---- BEGIN SSH2 PUBLIC KEY ----
    Comment: ""
    AAAAB3NzaC1yc2EAAAADAQABAAABAQCGjcJVVfGRfMWAcdVcOJSHsd1bphfaTWNM
    !!!!!!!!!!!THIS IS A FAKE PUBLIC KEY. PASTE YOUR OWN PUBLIC KEY 
    HERE AND MAKE SURE YOU DO NOT ADD CHARACTERS BY ACCIDENT!!!!!!!!
    !!!!!!!!!!59CFjWQ83NnTM5a2el4adblsc268XqE3Ts
    oA12mcKnbYu4iUltQazOayltKab6Nvz6YN/c5k+MppRu8pXDK/3UeZrwAZS5WrMj
    lQ1R3M/9o3ghy;ltedksyhodkgesygUVcyAv2yfPxoYf6HNUWwS4nw2OlRvI
    yWdChii0IlVbjhnNfprKmZUXzDfoxS+kUYGVin0VUG6heKXn0j9kNYZO3e069qVD
    JX7EMWeFfdOvxL6pGoMamEGrKJC53S+zzIdYGrQz5ilO/iAZ9U5d
    ---- END SSH2 PUBLIC KEY ----" >| /home/bitnami/.ssh/authorized_keys
    echo bitnami:yourstrongpasswordhere | chpasswd
    service sshd restart

(3) Click on the **Create instance** button at the bottom of the page.

Even after your new instance is created and is running, I found that you still need to give it a few more minutes before you can successfuly SSH into it using a password. Otherwise, it still gave me the "publickey" error.

To connect using a password, use the command:
    
    :::bash
    ssh bitnami@your-instance-ip

## Recovery

After you are able to login, check the `/home/bitnami/.ssh/authorized_keys` file to confirm that your new public key was added and that it is the only key there.

Next, you may need to disable password authentication to keep your instance secure. Open the `/etc/ssh/sshd_config` file and change the `PasswordAuthentication` setting back to `no`.
