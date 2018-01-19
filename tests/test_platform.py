from migen_misc.platforms import zedboard


def test_zedboard():
    plat = zedboard.Platform()
    assert len(plat.request("ps")) == 3
    assert len(plat.request("ddr")) == 73
