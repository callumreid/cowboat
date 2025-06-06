class Cowboat < Formula
  desc "Whimsical terminal animation of cows sailing away on boats"
  homepage "https://github.com/yourusername/cowboat"
  url "https://github.com/yourusername/cowboat/archive/v1.0.0.tar.gz"
  sha256 "REPLACE_WITH_ACTUAL_SHA256"
  license "MIT"

  depends_on "python@3.11"

  def install
    virtualenv_install_with_resources
  end

  test do
    system "#{bin}/cowboat", "--help"
  end
end 