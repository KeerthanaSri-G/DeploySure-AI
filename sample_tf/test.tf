resource "aws_security_group" "example" {
  ingress {
    cidr_blocks = ["0.0.0.0/0"]
  }
}

variable "aws_access_key" {
  default = "FAKEKEY123"
}