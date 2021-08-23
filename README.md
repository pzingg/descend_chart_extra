# DescendTreeExtra report addon


## Build

See https://www.gramps-project.org/wiki/index.php/Addons_development#Create_a_Gramps_Plugin_Registration_file

```
cd /home/pzingg/Projects/gramps-dev/addons-source
GRAMPSPATH=/home/pzingg/Projects/gramps-dev/gramps LANGUAGE=en_US.UTF-8 python3 make.py gramps51 build DescendTreeExtra
```

This should put DescendTreeExtra.addon.tgz into gramps-dev/addons/gramps51/download

## Create a listing

```
cd /home/pzingg/Projects/gramps-dev/addons-source # or wherever you have built your addon
GRAMPSPATH=/home/pzingg/Projects/gramps-dev/gramps LANGUAGE=en_US.UTF-8 python3 make.py gramps51 listing DescendTreeExtra
```

This will update all the locale files in gramps-dev/addons/gramps51/listings to include
the addon.

## Building and running gramps

```
cd /home/pzingg/Projects/gramps-dev/gramps
python3 setup.py build
cd /home/pzingg/Projects/gramps-dev/gramps/build/scripts-3.8
./gramps
```

## Installing addons

This doesn't work:
Go to Edit -> Preferences -> General
Change the URL in "Where to check:" to file:///home/pzingg/Projects/gramps-dev/addons/gramps51/

Instead unpack the .tgz built above, or copy files from addons-source into
/home/pzingg/.gramps/gramps51/plugins/DescendTreeExtra. For example:

```
cd /home/pzingg/.gramps/gramps51/plugins
tar xvzf /home/pzingg/Projects/gramps-dev/addons/gramps51/download/DescendTreeExtra.addon.tgz
```
