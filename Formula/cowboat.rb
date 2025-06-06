class Cowboat < Formula
  desc "Whimsical terminal animation of cows sailing away on boats"
  homepage "https://github.com/callumreid/cowboat"
  url "https://github.com/callumreid/cowboat/archive/v1.0.0.tar.gz"
  sha256 "74fa4a7cfbec6df3dd01aba409dd70eb30fc9021de40bc98115d3d83f5749f62"
  license "MIT"
  version "1.0.0"

  depends_on "python@3.11"

  def install
    bin.install "cowboat.py" => "cowboat"
  end

  test do
    system "#{bin}/cowboat", "--help"
  end
end 