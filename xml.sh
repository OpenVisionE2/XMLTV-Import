#!/bin/sh

cd etc/epgimport
wget -O russian.sources.xml https://raw.githubusercontent.com/doglover3920/EPGimport-Sources/main/russian.sources.xml
wget -O rytec.sources.xml https://raw.githubusercontent.com/doglover3920/EPGimport-Sources/main/rytec.sources.xml
wget -O spainKoala.sources.xml https://raw.githubusercontent.com/doglover3920/EPGimport-Sources/main/spainKoala.sources.xml
cd ..
cd ..
git add -u
git add *
git commit -m "Fetch latest doglover3920's xml files. (build $TRAVIS_BUILD_NUMBER)"
