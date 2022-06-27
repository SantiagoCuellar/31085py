#!/usr/bin/env bash

if [ $VIRTUAL_ENVIRONMENT ]
then
    deactivate
fi
. django/Scripts/activate