# Enable WSL 2 and Install a Linux Distribution:

  ## Open PowerShell as Administrator and run:

    wsl --install

   This command will enable WSL and install Ubuntu by default. You can choose a different distribution from the Microsoft Store if you prefer.

# Install Docker in WSL 2 Distribution:

   Open your WSL 2 terminal (e.g., Ubuntu).

    sudo apt update
    sudo apt install apt-transport-https ca-certificates curl software-properties-common
    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
    echo "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
    sudo apt update
    sudo apt install docker-ce docker-ce-cli containerd.io
    sudo apt install docker-compose
    sudo service docker start
    sudo usermod -aG docker $USER

