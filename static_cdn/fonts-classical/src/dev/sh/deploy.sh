#!/bin/bash

VERSION="1.0.1"
BRANCH="master"
REMOTE_ADDR="git@github.com:williamcanin/fonts-classical.git"
REMOTE_ADDR_ENABLE="yes"

function _PUSH_GITHUB(){

sed -i "s|^  \"version\":.*|  \"version\": \"${VERSION}\",|g" ./bower.json
sed -i "s|^  \"version\":.*|  \"version\": \"${VERSION}\",|g" ./src/dev/Grunt/package.json
sed -i "s|^  \"version\":.*|  \"version\": \"${VERSION}\",|g" ./src/dev/Gulp/package.json

if [[ "$REMOTE_ADDR_ENABLE" == "no" ]]; then
  git init
  git remote add origin $REMOTE_ADDR
  sed -i "s|^REMOTE_ADDR_ENABLE=.*|REMOTE_ADDR_ENABLE=\"yes\"|g" ./deploy
else
  printf "\nRemote already set address."
  printf "\nRemote: $REMOTE_ADDR\n\n"
fi
git status
printf "\nSee carefully configured file.\n"
printf "You want to continue? (Answer with the number)\n\n"
PS3="Reply >"
select runner in "Yes" "No"; do
case $runner in
  "Yes" )
    git add .
    printf "\nCommit message\n> "
    read COMMIT_MESSAGE
    git commit -m "$COMMIT_MESSAGE - Version $VERSION"
    git push origin $BRANCH
    printf "\nDone.\n\n"
    break
    ;;
   "No" )
      printf "\nCanceled by the user.\n\n"
      break
   ;;
   *)
      printf "\nInvalid Option\n\n"
   ;;
esac
done
}


function _PUSH_TAG_GITHUB(){

printf "\nInsert messege for version:\nMessage >"
read commit_msg_tag
git tag -a v$VERSION -m "$commit_msg_tag"

git tag -l
printf "\n[ Choose a tag ]\nInsert > "
read tagp
git push origin $tagp

}


case "$1" in
	push_deploy )
		_PUSH_GITHUB
		;;
	push_tag )
		_PUSH_TAG_GITHUB
		;;
	* )
		printf "\nUsage: $0 { push_deploy | push_tag }\n\n"
	;;
esac