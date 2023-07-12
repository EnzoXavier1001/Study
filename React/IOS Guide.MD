## 1. Install XCode and [Brew](https://brew.sh)
- *XCode:* App Store
    - `sudo xcode-select -switch /Applications/Xcode.app/Contents/Developer`
    - `xcodebuild -showsdks`
- *Brew:* run command line: 
    - `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`


## 2. Java
- Download it from [Java Web Site](https://www.java.com/en/download/)


## 3. RVM [Ruby Version Manager](https://rvm.io)
- `brew install gnupg`
- `curl -sSL https://rvm.io/mpapis.asc | gpg --import -`
- `curl -sSL https://rvm.io/pkuczynski.asc | gpg --import -`
- `\curl -sSL https://get.rvm.io | bash -s stable`
    or
    - `\curl https://raw.githubusercontent.com/rvm/rvm/master/binscripts/rvm-installer | bash -s stable`
- `rvm install 3.0`

## 4. [CocoaPods]()
- `sudo gem install cocoapods` (_If any error pops up just do what you are told_)
- `pod setup`
- `pod install` (_Inside de ios/ directory in the project_)