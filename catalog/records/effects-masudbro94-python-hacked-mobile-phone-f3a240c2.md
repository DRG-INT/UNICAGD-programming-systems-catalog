# Masudbro94/python-hacked-mobile-phone-

## Navigation

[Catalog index](../index.md) · [Language: Effects](../by-language/effects.md) · [Category: Build System](../by-category/build-system.md) · [Release watch](../release-watch.md) · [Apache/MIT license index](../license-index.md)

<!-- robots.txt: compliant -->
<!-- canonical: https://github.com/Masudbro94/python-hacked-mobile-phone- -->
<!-- crawl-delay: 10 -->

## Identity

| Field | Value |
| --- | --- |
| Language branch | Effects |
| Category | Build System |
| Source type | registry_expansion |
| Verification | registry-derived |
| Canonical URL | [https://github.com/Masudbro94/python-hacked-mobile-phone-](https://github.com/Masudbro94/python-hacked-mobile-phone-) |
| Source record ids | github_search_effects-f5dbe07a216424 |

## System Engineer Summary

Open in app Get started ITNEXT Published in ITNEXT You have 2 free member-only stories left this
month. Sign up for Medium and get an extra one Kush Kush Follow Apr 15, 2021 · 7 min read · Listen
Save How you can Control your Android Device with Python Photo by Caspar Camille Rubin on Unsplash
Photo by Caspar Camille Rubin on Unsplash Introduction A while back I was thinking of ways in which
I could annoy my friends by spamming them with messages for a few minutes, and while doing some
research I came across the Android Debug Bridge. In this quick guide I will show you how you can
interface with it using Python and how to create 2 quick scripts. The ADB (Android Debug Bridge) is
a command line tool (CLI) which can be used to control and communicate with an Android device. You
can do many things such as install apps, debug apps, find hidden features and use a shell to
interface with the device directly. To enable the ADB, your device must firstly have Developer
Options unlocked and USB debugging enabled. To unlock developer options, you can go to your devices
settings and scroll down to the about section and find the build number of the current software
which is on the device. Click the build number 7 times and Developer Options will be enabled. Then
you can go to the Developer Options panel in the settings and enable USB debugging from there. Now
the only other thing you need is a USB cable to connect your device to your computer. Here is what
todays journey will look like: Installing the requirements Getting started The basics of writing
scripts Creating a selfie timer Creating a definition searcher Installing the requirements The first
of the 2 things we need to install, is the ADB tool on our computer. This comes automatically
bundled with Android Studio, so if you already have that then do not worry. Otherwise, you can head
over to the official docs and at the top of the page there should be instructions on how to install
it. Once you have installed the ADB tool, you need to get the python library which we will use to
interface with the ADB and our device. You can install the pure-python-adb library using pip install
pure-python-adb. Optional: To make things easier for us while developing our scripts, we can install
an open-source program called scrcpy which allows us to display and control our android device with
our computer using a mouse and keyboard. To install it, you can head over to the Github repo and
download the correct version for your operating system (Windows, macOS or Linux). If you are on
Windows, then extract the zip file into a directory and add this directory to your path. This is so
we can access the program from anywhere on our system just by typing in scrcpy into our terminal
window. Getting started Now that all the dependencies are installed, we can start up our ADB and
connect our device. Firstly, connect your device to your PC with the USB cable, if USB debugging is
enabled then a message should pop up asking if it is okay for your PC to control the device, simply
answer yes. Then on your PC, open up a terminal window and start the ADB server by typing in adb
start-server. This should print out the following messages: * daemon not running; starting now at
tcp:5037 * daemon started successfully If you also installed scrcpy, then you can start that by just
typing scrcpy into the terminal. However, this will only work if you added it to your path,
otherwise you can open the executable by changing your terminal directory to the directory of where
you installed scrcpy and typing scrcpy.exe. Hopefully if everything works out, you should be able to
see your device on your PC and be able to control it using your mouse and keyboard. Now we can
create a new python file and check if we can find our connected device using the library: Here we
import the AdbClient class and create a client object using it. Then we can get a list of devices
connected. Lastly, we get the first device out of our list (it is generally the only one there if
there is only one device connected). The basics of writing scripts The main way we are going to
interface with our device is using the shell, through this we can send commands to simulate a touch
at a specific location or to swipe from A to B. To simulate screen touches (taps) we first need to
work out how the screen coordinates work. To help with these we can activate the pointer location
setting in the developer options. Once activated, wherever you touch on the screen, you can see that
the coordinates for that point appear at the top. The coordinate system works like this: A diagram
to show how the coordinate system works A diagram to show how the coordinate system works The top
left corner of the display has the x and y coordinates (0, 0) respectively, and the bottom right
corners’ coordinates are the largest possible values of x and y. Now that we know how the coordinate
system works, we need to check out the different commands we can run. I have made a list of commands
and how to use them below for quick reference: Input tap x y Input text “hello world!” Input
keyevent eventID Here is a list of some common eventID’s: 3: home button 4: back button 5: call 6:
end call 24: volume up 25: volume down 26: turn device on or off 27: open camera 64: open browser
66: enter 67: backspace 207: contacts 220: brightness down 221: brightness up 277: cut 278: copy
279: paste If you wanted to find more, here is a long list of them here. Creating a selfie timer Now
we know what we can do, let’s start doing it. In this first example I will show you how to create a
quick selfie timer. To get started we need to import our libraries and create a connect function to
connect to our device: You can see that the connect function is identical to the previous example of
how to connect to your device, except here we return the device and client objects for later use. In
our main code, we can call the connect function to retrieve the device and client objects. From
there we can open up the camera app, wait 5 seconds and take a photo. It’s really that simple! As I
said before, this is simply replicating what you would usually do, so thinking about how to do
things is best if you do them yourself manually first and write down the steps. Creating a
definition searcher We can do something a bit more complex now, and that is to ask the browser to
find the definition of a particular word and take a screenshot to save it on our computer. The basic
flow of this program will be as such: 1. Open the browser 2. Click the search bar 3. Enter the
search query 4. Wait a few seconds 5. Take a screenshot and save it But, before we get started, you
need to find the coordinates of your search bar in your default browser, you can use the method I
suggested earlier to find them easily. For me they were (440, 200). To start, we will have to import
the same libraries as before, and we will also have our same connect method. In our main function we
can call the connect function, as well as assign a variable to the x and y coordinates of our search
bar. Notice how this is a string and not a list or tuple, this is so we can easily incorporate the
coordinates into our shell command. We can also take an input from the user to see what word they
want to get the definition for: We will add that query to a full sentence which will then be
searched, this is so that we can always get the definition. After that we can open the browser and
input our search query into the search bar as such: Here we use the eventID 66 to simulate the press
of the enter key to execute our search. If you wanted to, you could change the wait timings per your
needs. Lastly, we will take a screenshot using the screencap method on our device object, and we can
save that as a .png file: Here we must open the file in the write bytes mode because the screencap
method returns bytes representing the image. If all went according to plan, you should have a quick
script which searches for a specific word. Here it is working on my phone: A GIF to show how the
definition searcher example works on my phone A GIF to show how the definition searcher example
works on my phone Final thoughts Hopefully you have learned something new today, personally I never
even knew this was a thing before I did some research into it. The cool thing is, that you can do
anything you normal would be able to do, and more since it just simulates your own touches and
actions! I hope you enjoyed the article and thank you for reading! 💖 468 9 468 9 More from ITNEXT
Follow ITNEXT is a platform for IT developers & software engineers to share knowledge, connect,
collaborate, learn and experience next-gen technologies. Sabrina Amrouche Sabrina Amrouche ·Apr 15,
2021 Using the Spotify Algorithm to Find High Energy Physics Particles Python 5 min read Using the
Spotify Algorithm to Find High Energy Physics Particles Wenkai Fan Wenkai Fan ·Apr 14, 2021
Responsive design at different levels in Flutter Flutter 3 min read Responsive design at different
levels in Flutter Abhishek Gupta Abhishek Gupta ·Apr 14, 2021 Getting started with Kafka and Rust:
Part 2 Kafka 9 min read Getting started with Kafka and Rust: Part 2 Adriano Raiano Adriano Raiano
·Apr 14, 2021 How to properly internationalize a React application using i18next React 17 min read
How to properly internationalize a React application using i18next Gary A. Stafford Gary A. Stafford
·Apr 14, 2021 AWS IoT Core for LoRaWAN, AWS IoT Analytics, and Amazon QuickSight Lora 11 min read
AWS IoT Core for LoRaWAN, Amazon IoT Analytics, and Amazon QuickSight Read more from ITNEXT
Recommended from Medium Morpheus Morpheus Morpheus Swap — Resurrection Ashutosh Kumar Ashutosh Kumar
GIT Branching strategies and GitFlow Balachandar Paulraj Balachandar Paulraj Delta Lake Clones:
Systematic Approach for Testing, Sharing data Jason Porter Jason Porter Week 3 -Yieldly No-Loss
Lottery Results Casino slot machines Mikolaj Szabó Mikolaj Szabó in HackerNoon.com Why functional
programming matters Tt Tt Set Up LaTeX on Mac OS X Sierra Goutham Pratapa Goutham Pratapa Upgrade
mongo to the latest build Julia Says Julia Says in Top Software Developers in the World How to
Choose a Software Vendor AboutHelpTermsPrivacy Get the Medium app A button that says 'Download on
the App Store', and if clicked it will lead you to the iOS App store A button that says 'Get it on,
Google Play', and if clicked it will lead you to the Google Play store

## Operational Role

For a systems engineer, Masudbro94/python-hacked-mobile-phone- belongs in the Effects inventory as
part of build graph control, artifact reproducibility, cross-platform build policy, and CI
integration.

## Release Intelligence

| Channel | Status | Version | Date | Source | Reason |
| --- | --- | --- | --- | --- | --- |
| stable | partial |  | 2022-06-30T09:10:26Z | gh search repos particle system | gh_search_reports_activity_not_release_version |
| preview/nightly | unknown |  |  | unknown | gh_search_has_no_standard_nightly_channel |

## License And Use Alert

| Field | Value |
| --- | --- |
| Detected family | Unknown license |
| Evidence | {"key": "", "name": "", "url": ""} |
| Alert | Backup plan required: license metadata is missing, so do not assume Apache or MIT compatibility. |

## Engineering Notes

- Treat category as `build_system` unless a later verified source gives a better classification.
- Keep provenance attached when merging duplicate identities; source evidence is not disposable.
- Stable release is unknown because `gh_search_reports_activity_not_release_version`.
- Preview/nightly metadata is unknown because `gh_search_has_no_standard_nightly_channel`.

## Provenance

<details>
<summary><strong>Provenance Details</strong> (click to expand)</summary>

| Kind | Status | Date | Detail |
| --- | --- | --- | --- |
| github_cli_search | forge-cli-derived | 2026-09-04 | `{"command": "gh search repos", "kind": "github_cli_search", "query": "particle system", "retrieved": "2026-09-04", "status": "forge-cli-derived"}` |

</details>

## Evidence

<details open>
<summary><strong>Evidence Records</strong> (click to collapse)</summary>

Evidence records merged into this identity: `1`.

- `github_search_effects-f5dbe07a216424` from `github_search_effects` as `registry_expansion`

</details>

## Related Records

| Name | Category | Page |
| --- | --- | --- |
| AuburnSounds/Dplug | Build System | [open](effects-auburnsounds-dplug-3c33ea8b.md) |
| c8r/iso | Build System | [open](effects-c8r-iso-4a2333dd.md) |
| ChrisBuilds/terminaltexteffects | Build System | [open](effects-chrisbuilds-terminaltexteffects-f3febb67.md) |
| CuarzoSoftware/Louvre | Build System | [open](effects-cuarzosoftware-louvre-8e4b81d1.md) |
| DatanoiseTV/PicoADK-Hardware | Build System | [open](effects-datanoisetv-picoadk-hardware-020ed462.md) |
| james34602/JamesDSPManager | Build System | [open](effects-james34602-jamesdspmanager-b977897f.md) |
| JatinChopra/emissive-dissolve-effect | Build System | [open](effects-jatinchopra-emissive-dissolve-effect-0dafd235.md) |
| kleineluka/junelite | Build System | [open](effects-kleineluka-junelite-95d9c2fb.md) |

## Category Index

[Api Abi Checker (213)](../by-category/api-abi-checker.md) · [Api Doc Generator (12)](../by-category/api-doc-generator.md) · [Assertion Mocking (46)](../by-category/assertion-mocking.md) · [Async Runtime (136)](../by-category/async-runtime.md)
[Benchmarking (191)](../by-category/benchmarking.md) · **[Build System (972)](../by-category/build-system.md)** · [Cli (553)](../by-category/cli.md) · [Codegen Codemod Refactoring (23)](../by-category/codegen-codemod-refactoring.md)
[Community Reference (116)](../by-category/community-reference.md) · [Compiler (175)](../by-category/compiler.md) · [Compiler Diagnostics (23)](../by-category/compiler-diagnostics.md) · [Compression (50)](../by-category/compression.md)
[Concurrency Parallelism (88)](../by-category/concurrency-parallelism.md) · [Configuration (125)](../by-category/configuration.md) · [Container Deployment (9)](../by-category/container-deployment.md) · [Coverage (14)](../by-category/coverage.md)
[Cryptography (172)](../by-category/cryptography.md) · [Data Science (37)](../by-category/data-science.md) · [Database Datastore (884)](../by-category/database-datastore.md) · [Datetime (213)](../by-category/datetime.md)
[Dead Code Dependency Analysis (5)](../by-category/dead-code-dependency-analysis.md) · [Debugger (44)](../by-category/debugger.md) · [Dependency Manager (101)](../by-category/dependency-manager.md) · [Documentation (103)](../by-category/documentation.md)
[Embedded Hardware (56)](../by-category/embedded-hardware.md) · [Ffi Bindings (446)](../by-category/ffi-bindings.md) · [Filesystem Os (1535)](../by-category/filesystem-os.md) · [Formatter (634)](../by-category/formatter.md)
[Framework (61)](../by-category/framework.md) · [Fuzzer (57)](../by-category/fuzzer.md) · [Game Engine Game Dev (353)](../by-category/game-engine-game-dev.md) · [Ide Editor Integration (1415)](../by-category/ide-editor-integration.md)
[Image Audio Dsp (419)](../by-category/image-audio-dsp.md) · [Interop Bindings (61)](../by-category/interop-bindings.md) · [Interpreter Runtime (265)](../by-category/interpreter-runtime.md) · [Jit Vm (62)](../by-category/jit-vm.md)
[Language Server (28)](../by-category/language-server.md) · [Language Specification (1421)](../by-category/language-specification.md) · [Library (5475)](../by-category/library.md) · [Lint Plugin (1)](../by-category/lint-plugin.md)
[Lint Rule Pack (48)](../by-category/lint-rule-pack.md) · [Linter (348)](../by-category/linter.md) · [Logging Observability (515)](../by-category/logging-observability.md) · [Machine Learning (740)](../by-category/machine-learning.md)
[Math Numeric Scientific (87)](../by-category/math-numeric-scientific.md) · [Memory Analyzer (95)](../by-category/memory-analyzer.md) · [Message Broker (40)](../by-category/message-broker.md) · [Networking Http (1016)](../by-category/networking-http.md)
[Other (14)](../by-category/other.md) · [Package Manager (435)](../by-category/package-manager.md) · [Parser Lexer Ast (1072)](../by-category/parser-lexer-ast.md) · [Precommit Ci Quality (294)](../by-category/precommit-ci-quality.md)
[Profiler (86)](../by-category/profiler.md) · [Project Scaffolding (132)](../by-category/project-scaffolding.md) · [Registry Repository (132)](../by-category/registry-repository.md) · [Sanitizer (13)](../by-category/sanitizer.md)
[Security Sast (336)](../by-category/security-sast.md) · [Serialization (391)](../by-category/serialization.md) · [Standard Library (25)](../by-category/standard-library.md) · [Static Analyzer (525)](../by-category/static-analyzer.md)
[Templating (2)](../by-category/templating.md) · [Testing Framework (599)](../by-category/testing-framework.md) · [Tutorial Book Styleguide (62)](../by-category/tutorial-book-styleguide.md) · [Type Checker (311)](../by-category/type-checker.md)
[Undefined Behavior Analyzer (1574)](../by-category/undefined-behavior-analyzer.md) · [Utility Library (102)](../by-category/utility-library.md) · [Visualization Gui (513)](../by-category/visualization-gui.md) · [Web Framework (473)](../by-category/web-framework.md)
