#!/usr/bin/env bash
# using puppet to change configuration file

file { 'ect/ssh/ssh_config':
        ensure => present,
        
content =>"

        #SSH clint configuration
        host*
        IdentityFile ~/.ssh/school
        PasswordAuthentication no
        ",
        
}
