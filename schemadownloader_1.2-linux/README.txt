## SchemaDownloader

`SchemaDownloader` is a standalone tool that is used for obtaining a blpapi service schema for mocking blpapi events.
It is a statically linked binary that supports Linux and Windows operating systems for both 32 and 64 bits.


### Usage

```
General:
  -h, --help            Show this help message and exit

Usage:
  -H, --host host:port[/socks5Host:socks5Port]
                        Endpoint host:port and optional SOCKS5 host:port to use to connect (default: localhost:8194).
  -s, --service service
                        Service name for schema download
  --file outputFile
                        Output file name (default: schema.xsd)

TLS (specify all or none):
  --tls-client-credentials file
                        name a PKCS#12 file to use as a source of client credentials
  --tls-client-credentials-password password
                        specify password for accessing client credentials
  --tls-trust-material file
                        name a PKCS#7 file to use as a source of trusted certificates
  --read-certificate-files
                        read the TLS files and pass the blobs

ZFP connections over leased lines (requires TLS):
  --zfp-over-leased-line port
                        enable ZFP connections over leased lines on the specified port (8194 or 8196)
                        (When this option is enabled, option -H/--host is ignored.)
```

**Note** that `--zfp-over-leased-line` cannot be used in conjunction with the `--host` option.