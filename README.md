# ChatRoom

Auteurs : Stanyslas LACHAUD & Nathan PLACE

Version : 1.0

Langage : Python 3 (bibliothèque standard uniquement)


Présentation

ChatRoom est un serveur de chat en temps réel basé sur les sockets TCP et le multithreading. Chaque client connecté dispose de son propre fil d'exécution, ce qui permet de gérer plusieurs connexions simultanées sans blocage.


Prérequis


Python 3.x installé sur la machine serveur (Linux recommandé)
Aucune dépendance externe — uniquement socket et threading (bibliothèque standard)
Les deux machines doivent être sur le même réseau (local ou VPN)



Lancer le serveur

bashpython3 chatroom.py

Le serveur écoute par défaut sur le port 1966 (toutes interfaces : 0.0.0.0).


Se connecter en tant que client

Depuis n'importe quelle machine sur le même réseau, utiliser netcat :

bashnc <IP_DU_SERVEUR> 1966

Exemples :

bash# Réseau local
nc 192.168.1.134 1966

# Via ZeroTier ou Tailscale (voir section VPN ci-dessous)
nc 10.147.20.x 1966


Utilisation à distance — VPN

Si les machines ne sont pas sur le même réseau local, il faut passer par un VPN overlay pour que le serveur soit joignable.

Option 1 — ZeroTier (recommandé pour des tests entre plusieurs personnes)


Créer un réseau sur https://my.zerotier.com
Installer ZeroTier sur chaque machine :


bash   # Debian/Ubuntu
   curl -s https://install.zerotier.com | sudo bash


Rejoindre le réseau :


bash   sudo zerotier-cli join <NETWORK_ID>


Autoriser les machines dans l'interface ZeroTier
Récupérer l'IP ZeroTier de la machine serveur (sudo zerotier-cli listnetworks) et s'y connecter avec netcat


Option 2 — Tailscale (plus simple pour un binôme)


Installer Tailscale : https://tailscale.com/download
Se connecter avec un compte (Google, GitHub, etc.)
Les deux machines apparaissent dans le même réseau Tailscale
Utiliser l'IP Tailscale de la machine serveur (visible via sudo tailscale status)



Cartographie du réseau (exemple)

MachineInterface réseauAdresse IPRôleServeur hôtelocale / VPN192.168.1.134 / 100.x.x.xLance chatroom.pyClient 1locale / VPN192.168.1.x / 100.x.x.xnc vers le serveurClient 2locale / VPN192.168.1.x / 100.x.x.xnc vers le serveur


Limitations connues


La liste des utilisateurs est partagée entre threads sans verrou (threading.Lock) : une race condition est possible si plusieurs clients se déconnectent simultanément. Correction prévue.
Pas d'authentification : tout client qui se connecte peut envoyer des messages.
Les messages ne sont pas persistés (pas d'historique).
