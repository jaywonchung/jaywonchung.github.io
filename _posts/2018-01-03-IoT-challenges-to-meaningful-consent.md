---
title: "[Review] The Internet of Things: Interaction Challenges to Meaningful Consent at Scale"
excerpt: "ACM Interactions Nov+Dec 2017. On adopting the IoT technology, how should we be prepared in terms of giving out our information?"
categories:
  - read
  - magazines
---
## Article
[The Internet of Things: Interaction Challenges to Meaningful Consent at Scale (ACM Interactions, Volume 24 Issue 6, Nov+Dec 2017)](https://dl.acm.org/citation.cfm?id=3149025)

## Background
### Public-Key Cryptography
Also called asymmetrical cryptography. Using a pair of keys (a public key and a private key), it can be used for encryption and authentication. The former is done by encrypting the message with the public key, which can be seen by anyone. A message encrypted with the public key can only be decrypted with its pair private key. The latter, authentication, is done in the opposite direction; a message is signed with the private key, and anyone with a public key can verify that the sender is the owner of the private key.

### Public-Key Infrastructure
A Certification Authority (CA) issues Public Key Certificates  (a.k.a. digital certificates), which is essentially a trustworthy identity of a user. A client receiving the certificate can get an assurance that he is talking to the real user by checking the digital signature with the public key provided. The certificate has a lifecycle which is controlled by the Certificate Managing System, which publishes, suspends, renews, and revokes certificates.

### HTTPS
HTTP (HypterText Transfer Protocol) is inadequate for transferring information that should be kept secure. Thus a new protocol HTTPS (HTTP + Security) came up, which is HTTP working over SSL/TLS encryption, HTTPS uses digital certificates to assure the client the following: that all traffic is encrypted, that the traffic is not altered on the way, and that he is talking to the real website. When connecting to an https:// website, the web browser is presented with a digital certificate. The browser checks if the certificate matches the website. If it's valid, and if it was issued by a CA the browser trusts, we are safely connected to that website. now the browser encrypts its transactions with the public key obtained from the certificate.

## Summary and Review
Computer science nowadays should, ironically, be more human-centered than ever, following the rapid advancements of IoT (Internet of Things). IoT is more than just an explosion of the number of devices connected to the web; it entails differences in terms of social, economic lives of people, the laws that control it, and the technological model engineers have, and it should be humans that center the change. There are many issues to be solved, and one of it is to establish a meaningful consent over the flow of information.

We thoughtlessly click "I Agree." when we see a terms and conditions page or an alert that says "Our page uses cookies", without trying to know what information we are disclosing to the service provider and how it is used. After all, it's nearly impossible to read through the terms and conditions given to us since it is written in highly sophisticated language well exceeding the norm of the people using the service.

Since we want and need to choose who gets our data and who doesn't the flow of information should be apparent, and semantically and pragmatically transparent to us. Apparency is whether we know how a data activity is signaled, semantic transparency is whether we understand the terms related to it, and pragmatic transparency is the degree to which we know what these data actions actually to or entail.

In addition, when IoT becomes prominent and our lives immersed in a plethora of internet-connected devices, our consent on data/personal information may be assumed given. Innocuous bits of data we drop on the web may combine to de-anonymize our identity. Thus we need mechanisms that can negotiate our consent on our behalf.

For this, let us address several points of analysis.
1. We should know how 'users' model IoT apparency and s/p transparency. Without a good understanding of how citizens think is happening with all those devices, we cannot design human-centered and safe mechanisms.
2. We should understand how users' and designers' models are different. For instance, a user traditionally expects to 'own' a hardware he or she purchases. However, in an IoT engineer's perspective, it may merely be part of a vast IoT network, sometimes controlled for the good of the whole network.
3. Users should be able to form adequate models of device ecosystems and their infrastructure. One important variable here is time. Most consents now are given based on the assumption that things mostly remain similar in the future. With time better considered, consent for data use can be far more meaningful.
