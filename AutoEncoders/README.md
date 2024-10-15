# Autoencoder Architectures and Metrics

This repository contains the architecture of various autoencoders.
---
### 1. Simple Autoencoder
| **Metric**   | **Image** |
|--------------|-----------|
| **Training Loss:** | <img width="80%" style="max-height: 350px;" alt="simple_autoencoder_training_loss" src="../images/simple_autoencoder_training_loss.svg"> |
| **Validation Loss:** | <img width="80%" style="max-height: 350px;" alt="simple_autoencoder_validation_loss" src="../images/simple_autoencoder_validation_loss.svg"> |
<br>

**Reconstructed Images:**

<img  style="width:400px; height: 350px;" alt="simple_autoencoder_gen_images" src="../images/simple_autoencoder_gen_images.png"> 
---

### 2. Convolutional Autoencoder
| **Metric**   | **Image** |
|--------------|-----------|
| **Training Loss (Per Batch):** | <img width="80%" style="max-height: 350px;" alt="ConvAutoEncoder_Train_Loss_Per_Batch" src="../images/ConvAutoEncoder_Train_Loss_Per_Batch.svg"> |
| **Training Loss (Per Epoch):** | <img width="80%" style="max-height: 350px;" alt="ConvAutoEncoder_Train_Loss_Per_Epoch" src="../images/ConvAutoEncoder_Train_Loss_Per_Epoch.svg"> |
| **Validation Loss (Per Batch):** | <img width="80%" style="max-height: 350px;" alt="ConvAutoEncoder_Validation_Loss_Per_Batch" src="../images/ConvAutoEncoder_Validation_Loss_Per_Batch.svg"> |
| **Validation Loss (Per Epoch):** | <img width="80%" style="max-height: 350px;" alt="ConvAutoEncoder_Validation_Loss_Per_Epoch" src="../images/ConvAutoEncoder_Validation_Loss_Per_Epoch.svg"> |

<br>

**Reconstructed Images**

<img width="80%" style="max-height: 350px;" alt="ConvAutoEncoder-Reconstructed_Images" src="../images/ConvAutoEncoder_Reconstructed_Images.png">
---


### 3. Variational Autoencoder (VAE)
***Orange***: experiment-1, ***Blue***: experiment-2 |

| **Metric**   | **Image** |
|--------------|-----------|
| **Training Loss (Per Batch):** | <img width="80%" style="max-height: 350px;" alt="VAE_Train_Loss_Per_Batch" src="../images/VAE_Train_Loss_Per_Batch.svg"> |
| **Training Loss (Per Epoch):** | <img width="80%" style="max-height: 350px;" alt="VAE_Train_Loss_Per_Epoch" src="../images/VAE_Train_Loss_Per_Epoch.svg"> |
| **Validation Loss (Per Batch):** | <img width="80%" style="max-height: 350px;" alt="VAE_Validation_Loss_Per_Batch" src="../images/VAE_Validation_Loss_Per_Batch.svg"> |
| **Validation Loss (Per Epoch):** | <img width="80%" style="max-height: 350px;" alt="VAE_Validation_Loss_Per_Epoch" src="../images/VAE_Validation_Loss_Per_Epoch.svg"> |

<br>
| **Metric**   | **Image** |
| **KL Divergence Loss:** | <img width="80%" style="max-height: 350px;" alt="VAE_KL_Divergence_Loss" src="../images/VAE_KL_Divergence_Loss.svg"> |
| **Reconstruction Loss:** | <img width="80%" style="max-height: 350px;" alt="VAE_Reconstruction_Loss" src="../images/VAE_Reconstruction_Loss.svg"> |
| **Total Loss:** | <img width="80%" style="max-height: 350px;" alt="VAE_Total_Loss" src="../images/VAE_Total_Loss.svg"> |

<br>

**Generated and Reconstructed Images**

| **Category** | **Image** |
|--------------|-----------|
| **Sampled from Latent Space:** | <img width="80%" style="max-height: 350px;" alt="vae_sampled_latent_space" src="../images/sampled-from-latent-space.png"> |
| **Generated Images:** | <img width="80%" style="max-height: 350px;" alt="vae_generated_images" src="../images/vae_generated_images.png"> |
| **Reconstructed Images:** | <img width="80%" style="max-height: 350px;" alt="vae_reconstructed_images" src="../images/ConvAutoEncoder_Reconstructed_Images.png"> |

---

This layout provides a clean and organized structure for displaying the metrics and generated images related to your Variational Autoencoder (VAE). Make sure that all image paths match the actual location in your repository. Let me know if you need further adjustments!