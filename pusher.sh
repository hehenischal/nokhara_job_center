#!/bin/bash

echo "Enter commit message:"
read -r commit_message

if [ -z "$commit_message" ]; then
    echo "Error: Commit message cannot be empty"
    exit 1
fi

git add .
git commit -m "$commit_message"
git push origin main

echo "Changes pushed successfully!"
