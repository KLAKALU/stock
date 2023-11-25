package main

import (
	"fmt"
	"os"
)

func isSshdirExist() bool {
	directlyPath := "~/.ssh"
	if _, err := os.Stat(directlyPath); err != nil {
		// ~/.ssh directory not exist
		fmt.Println("ssh-key directory not exist")
		return false
	}
	fmt.Println("ssh-key directory already exist")
	return true
}

func main() {
	path, err := os.Getwd()
	if err != nil {
		fmt.Println(err)
	}
	fmt.Println(path)
	homedir, err := os.UserHomeDir()
	if err != nil {
		fmt.Println(err)
	}
	fmt.Println(homedir)
	isSshdirExist()
	//filename := "go.mod"
	sshKeyPath := "/style.css"
	if _, err := os.Stat(sshKeyPath); err == nil {
		fmt.Println("ファイルは存在します")
	} else {
		fmt.Println("ファイルは存在しません")
	}
}
