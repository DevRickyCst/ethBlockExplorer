
// Detect if metamask account is changed
window.ethereum.on('accountsChanged', async () => {
    // Appel le back pour ajouter le compte dans les var de session
    fetch('delete-cookie',{
        method:"POST",
    })
    .then(response => response.json())
    .then(data => console.log('Réponse du serveur:', data))
    .catch(error => console.error('La requête a échoué. Erreur:', error));


    // Demander à l'utilisateur de se connecter à son compte MetaMask
    ethereum.request({ method: 'eth_requestAccounts' })

    .then(accounts => {

        // L'utilisateur est connecté avec succès
        console.log('Connected to account:', accounts[0]);

        // Appel le back pour ajouter le compte dans les var de session
        fetch('/set-cookie',{
            method:"POST",
            headers: {
                'Content-Type':'application/json',
            },
            body: JSON.stringify({'account':accounts[0]})
        })
        .then(response => response.json())
        .then(data => console.log('Réponse du serveur:', data))
        .catch(error => console.error('La requête a échoué. Erreur:', error));


        //Todo : 'Meilleur idée ?'
        // Redirection ver login redirection.
        fetch('/',{
            method:"GET",
        })
        .then(
            response => {
                    window.location = response.url
            }
        )
    })
});



function connectToMetamask(event){ 

// Vérifier si MetaMask est installé et actif
if (typeof window.ethereum !== 'undefined') {
    console.log('Metamask is installed!');

    // Demander à l'utilisateur de se connecter à son compte MetaMask
    ethereum.request({ method: 'eth_requestAccounts' })

        .then(accounts => {

        // L'utilisateur est connecté avec succès
        console.log('Connected to account:', accounts[0]);
        // Appel le back pour ajouter le compte dans les var de session
        fetch('/set-cookie',{
            method:"POST",
            headers: {
                'Content-Type':'application/json',
            },
            body: JSON.stringify({
                'account':accounts[0],
                'networkId': ethereum.networkVersion
            })
        })
        .then(response => response.json())
        .then(data => console.log('Réponse du serveur:', data))
        .catch(error => console.error('La requête a échoué. Erreur:', error))
        .then(
            window.location.reload()
        )
        })

        // La connexion a échoué
        .catch(error => {

        console.log('Connection error:', error);
        });
}
else {
    // MetaMask n'est pas installé, demander à l'utilisateur de l'installer
    console.log('Metamask is not installed.');
}
}


function deconnectToMetamask(event){ 
        // Appel le back pour ajouter le compte dans les var de session
        fetch('delete-cookie',{
            method:"POST",
        })
        .then(response => response.json())
        .then(data => console.log('Réponse du serveur:', data))
        .catch(error => console.error('La requête a échoué. Erreur:', error))
        .then(
            window.location.reload()
        )
}

document.addEventListener('DOMContentLoaded', function() {
    // Attach event listener to form submission
    document.getElementById('ethForm').addEventListener('submit', function(event) {
        event.preventDefault(); // Prevent default form submission
        
        // Call sendEth function
        sendEth();
    });

    // Function to send ETH
    function sendEth() {
        var ethAmount = document.getElementById("ethAmount").value;
        var recipientAddress = document.getElementById("recipientAddress").value;

        // Check if fields are filled
        if (ethAmount === "" || recipientAddress === "") {
            alert("Please fill in all fields.");
            return;
        }

        // Convert ETH amount to Wei
        var ethAmountWei = web3.utils.toWei(ethAmount, 'ether');

        // Send transaction to MetaMask
        web3.eth.sendTransaction({
            to: recipientAddress,
            value: ethAmountWei
        })
        .on('transactionHash', function(hash){
            console.log("Transaction hash:", hash);
            alert("Transaction sent successfully! Transaction hash: " + hash);
        })
        .on('error', function(error){
            console.error("Transaction error:", error);
            alert("Transaction error: " + error.message);
        });
    }
});