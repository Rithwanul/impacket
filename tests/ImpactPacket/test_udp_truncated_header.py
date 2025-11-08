import pytest
import traceback
from impacket import ImpactPacket

@pytest.mark.remote
def test_truncated_udp_header_load_show_error():
    """
    Show the actual error and traceback when loading a truncated UDP header.
    """
    print("\nAttempting to load truncated UDP header...")
    pkt = ImpactPacket.UDP()
    raw_data = b'\x00\x35'  
    # raw_data = b'\x00\x05\x05\x05\x05\x05\x05\x05\x01\x05s\x05\x05\x05\x05q\x03\x05\x05\x05\x05p\x01\x05\x05'

    try:
        pkt.load_header(raw_data)
        print("load_header() executed successfully (no error)")
    except Exception as e:
        print("\nCaught exception while loading truncated UDP header:")
        print(f"Type: {type(e).__name__}")
        print(f"Message: {e}")
        print("\nTraceback:")
        traceback.print_exc()
        # Stop here so pytest marks as passed
        return
