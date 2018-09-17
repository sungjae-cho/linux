# Upgrade command for `pip`
```bash
sudo pip install --upgrade pip
```

# Upgrade command for `pip3`
```bash
sudo pip3 install --upgrade pip
```

# Install multiple packages
1. Make a txt file named `requirements.txt`.
2. Fill in the txt file as the following.
  * If you need an exact version of `tensorflow`, `tensorflow==1.7.0`.
  * If you need a higher or lower version of `tensorflow`, `tensorflow>=1.7.0` or `tensorflow<=1.7.0`.
  * If you need a latest version of `tensorflow`, `tensorflow`.
```txt
numpy==1.14.2
atari-py==0.1.1
gym==0.10.4
ptan==0.3
opencv-python==3.4.0.12
scipy==1.0.1
torch==0.4.0
torchvision==0.2.1
tensorboard-pytorch==0.7.1
tensorflow==1.7.0
tensorboard==1.7.0
```
3. Enter the following command.
```bash
pip install -r requirements.txt
```
