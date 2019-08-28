********
Overview
********

This package is intended to quality control temperature and salinity profiles by applying a sequence of tests.
For CTD profiles and TSG timeseries it uses the `PySeabird package <http://seabird.castelao.net>`_, so it can interpret directly the SeaBird's .cnv output file.

This is the result from several generations of quality control systems,
which started in 2006, while I was responsible for the quality control of
the thermosalinographs at AOML-NOAA, USA. Later I was advising the quality
control of the brazilian hydrography of PIRATA, and currently I am working with
Quality Control of underwater gliders and the project IQuOD.

CoTeDe can apply different quality control procedures:
  - The default GTSPP or EGOOS procedure;
  - A custom set of tests, including user defined thresholds;
  - A novel approach based on Anomaly Detection, described by `Castelao 2015 <http://arxiv.org/abs/1503.02714>`_;

.. note::

    On version 0.20 there was an inversion of roles and instead of depending on
    PySeabird, now CoTeDe is an independent package that can be installed as an
    extra-requirement of PySeabird. The functionalities to quality control CTD
    and TSG are now in the package PySeabird. This allowed CoTeDe to focus on
    QC and better generalize for other platforms and instruments.

My opinion on quality control
-----------------------------

Quality control is different than data processing. 
On the processed data, the quality control/quality assurance means to classify what looks fine. 
It is very important that the data is properly sampled and processed. 
If all you have is bad data, quality control procedures can't go back on time and fix improper sampling, but only tell you that the data might not be good.

Once I was requested to quality control over 10 years of hydrographic data. 
It didn't take long to learn that all those cruises lack the proper procedure, which did compromise the data. 
That was not a quality control job, but data mining, in the sense of trying to rescue the most I could.
A CTD cast is far easier than reaching the moon, but there is a proper way to do it.

Why the name CoTeDe?
--------------------

Since NOAA I wanted to combine the multiple tests, but I didn't really knew how  to do that. 
In 2011 I learned the anomaly detection technique, but I only formalize the procedure in 2013, when I spent few months in Toulouse.
The full name of this package is CoTe De l'eau, which I believe it is something near to "rating the water". 
The short name is cotede, to make easier for the users to remember, since it is the quality control of COnductivity TEmperature and DEpth (cotede). 
The french name is a kind of tribute to the great time that I spent in France with Bia and the croissants that were converted in code lines.
