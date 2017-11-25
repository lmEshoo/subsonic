# subsonic

<p align="center">
  <br>
  <img src="https://s3.amazonaws.com/logo-lmeshoo/sub-music.lmeshoo.net.png">
</p>

## Prerequisites

- Setup the below environment variables before running anything

```bash
export SPOTIPY_CLIENT_ID=
export SPOTIPY_CLIENT_SECRET=
export SPOTIPY_OATH_TOKEN=
export SPOTIPY_REDIRECT_URI='http://0.0.0.0/'
export AWS_SUB_ACCESS_KEY_ID=
export AWS_SUB_SECRET_ACCESS_KEY=
export INSTANCE_IP=
export SUB_USER='admin'
export SUB_PASS='admin'
```

- Make sure your `.pem` file for AWS is in root directory.

## Usage

```bash
make start
```

**Note: Make sure your aws credentials are set**
