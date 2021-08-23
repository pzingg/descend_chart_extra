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