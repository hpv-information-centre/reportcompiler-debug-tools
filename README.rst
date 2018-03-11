Debugging tools for the Report Compiler
###################################

The debugging tools for the Report Compiler provide an interface to easily debug the context generation of failed report fragments
in different programming languages, preserving the original parameters that caused the errors and speeding up report development.

These tools are intended to be used as standalone scripts in an IDE/debugger like RStudio (for R)
or PyCharm (for python), for example. For this reason this multilanguage project is not offered as a package.

This project is being developed by the ICO/IARC Information Centre on HPV and Cancer 
and will be used in our report generation tasks.

.. image:: HPV_infocentre.png
   :height: 50px
   :align: center
   :target: http://www.hpvcentre.net

Features
============

* Hassle-free debugging for Report Compiler document generation.
* Usable from any IDE/debugger.
* Support for multiple languages.

How to use
==========

When generating documents with the parameter *debug_mode* set to True, the Report Compiler library 
automatically generates debugging information for the failed fragment generation processes in the 
*_meta* directory inside the reports path (specified by environment variable REPORTS_PATH). The 
scripts in this project call the failed generators with the exact same parameters as they were
called on the original document generation. Thus, source files can be easily and quickly debugged.

To summarize, the intended use case is:

1. Run document generation via the Report Compiler library with *debug_mode = True*.
2. If any context generation process fails, set breakpoints with your debugger of choice in the 
   desired source files.
3. Run the debug script associated to the generator programming language (e.g. r/debug.r).

Installation
============

Git hooks setup
---------------

.. code:: bash

 scripts/prepare_hooks.sh