resource "aws_s3_bucket" "unsecure_bucket" {
  bucket = "my-unsecure-bucket"
  acl    = "public-read"  # ❌ Misconfig: Public bucket
}

resource "aws_security_group" "open_sg" {
  name        = "open_sg"
  description = "Open to all"
  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]  # ❌ Misconfig: SSH open to the world
  }
}