# Hourglass Tree report addon for Gramps genealogy software

This report addon combines an ancestor tree and a descendant
tree into one chart, with ancestors on the left and descendants
to the right.

For the purposes of this README, we assume that these environment
variables have been set:

* "GRAMPS_CONF_DIR" will be the user-specific directory where Gramps stores
  its databases, reads its  preferences and from which addons are loaded at
  startup. It is usually "$HOME/.gramps"

* "GRAMPS_DEV_HOME" will be the directory into which you have cloned
  the "gramps", "addons", and "addons-source" repositories
  from the Gramps GitHub site.

* "GRAMPSPATH" will then be "$GRAMPS_DEV_HOME/gramps"

* "LANGUAGE" will be "en_US.UTF-8"

* The target Gramps version we will target builds for is 5.1, so
  relevant paths discussed below will be "gramps51".

## General notes

The main documentation for creating Gramps addons is at
https://www.gramps-project.org/wiki/index.php/Addons_development#Create_a_Gramps_Plugin_Registration_file

This addon was made by combining source code from two plugins
that are included in the base Gramps distribution:

* "gramps/plugins/drawreport/descendtree.py", and
* "gramps/plugins/drawreport/ancestortree.py"

The ancestor tree source was slightly modified to go from
left to right in descendant order from the original right to left.

Then both trees are built, and one is connected to the other
in the function `MakePersonTree.link_ancestors_to_center`.

## Download

To begin, clone this repository with

```
git clone https://github.com/pzingg/gramps_hourglass_tree \
  ${GRAMPS_DEV_HOME}/addons-source/HourglassTree
```

By convention, addon directories are capitalized, in camel case, without
spaces or other punctuation, so the directory containing this README and the
two Python source files should be "${GRAMPS_DEV_HOME}/addons-source/HourglassTree".

## Build

If you want to publish an addon you need to include it in the
locale-specific listing files maintained by Gramps. You don't need
to do this step if you are just running the addon locally, with
manual installation.

```
cd ${GRAMPS_DEV_HOME}/addons-source

# GRAMPSPATH and LANGUAGE must be set as above in order to use make.py
# Change gramps51 to something else for different targets
python3 make.py gramps51 build HourglassTree
```

This should put the archived addon file "HourglassTree.addon.tgz" into
"${GRAMPS_DEV_HOME}/addons/gramps51/download".

## Create a listing

If you want to publish an addon you need to include it in the
locale-specific listing files maintained by Gramps. You don't need
to do this step if you are just running the addon locally, with
manual installation.

```
cd ${GRAMPS_DEV_HOME}/addons-source

# GRAMPSPATH and LANGUAGE must be set as above in order to use make.py
# Change gramps51 to something else for different targets
python3 make.py gramps51 listing HourglassTree
```

This will update all the locale files in
"${GRAMPS_DEV_HOME}/addons/gramps51/listings" to include the addon.

## Building and running gramps

```
# Compile and build
cd ${GRAMPS_DEV_HOME}/gramps
python3 setup.py build

# Run the compiled Gramps application
# scripts-3.8 may be different if you have a different Python version
${GRAMPS_DEV_HOME}/gramps/build/scripts-3.8/gramps
```

## Installing addons

Changing the addon download and listing path preference in Gramps to your
development setup doesn't seem to work.  I tried this (expanding
"$GRAMPS_DEV_HOME" to the actual directory):

1. Go to "Edit" -> "Preferences" -> "General"
2. Change the value of "Where to check:" from the default "http://" URL to
    "file://${GRAMPS_DEV_HOME}/addons/gramps51/"


I also tried just "${GRAMPS_DEV_HOME}/addons/gramps51/" without the "file://"

Instead it's simpler to install the addon manually.

Either unpack the archived .tgz built above:

```
mkdir -p ${GRAMPS_CONF_DIR}/gramps51/plugins
tar xzf ${GRAMPS_DEV_HOME}/addons/gramps51/download/HourglassTree.addon.tgz \
  -C ${GRAMPS_CONF_DIR}/gramps51/plugins
```

Or just copy the two Python files from addons-source:

```
mkdir -p ${GRAMPS_CONF_DIR}/gramps51/plugins/HourglassTree
cp ${GRAMPS_DEV_HOME}/addons-source/HourglassTree/*.py ${GRAMPS_CONF_DIR}/gramps51/plugins/HourglassTree
```

Then restart Gramps.

Note: The Python files "hourglasstree.py" and "hourglasstree.gpr.py" should be
located in "${GRAMPS_CONF_DIR}/gramps51/plugins/HourglassTree", and
the `status` option in "hourglasstree.gpr.py" must be set to "STABLE",
in order for the addon to be loaded at startup.

## Other notes

For proper functioning, you may need to have the "show_parents" option set.

### Gramps report display options

Here's the substitution cheat sheet page:

https://gramps-project.org/wiki/index.php/Gramps_5.1_Wiki_Manual_-_Reports_-_part_2

As an example, the following report dispay option will show nicknames,
like "Nick / First Middle Last"; and birth and death dates and places,
like "b. 12 Dec 1985 in San Francisco" (if the place has been edited
to be a "City" type).

```
$n(n< / >f< >l)
b. $b {in $B(c)}
-{d. $d} {in $D(c)}
```

And for the marriage places:

```
m. $m {in $M(c)}
```

In order to see the cities (`$B(c)`, `$D(c)`, `$M(c)`, etc), the places
must be correctly structured. One way is to go through each place that has
the "Unknown" place type with the "Place Cleanup" gramplet.

First you set up a Geonames account with public access, then install
and use the gramplet. Instructions are here:

https://www.gramps-project.org/wiki/index.php/Addon:PlaceCleanupGramplet#Installing_the_Place_Cleanup_Gramplet
