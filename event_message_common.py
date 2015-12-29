EPCC_EXPERIMENTER_ID = 0xEBCC3118
EVT_SUBTYPE_STRING = "!II"
EVT_HEADER_SIZE = 8

EVT_SUBTYPE_EVENT_REQUEST = 0x00
EVT_SUBTYPE_EVENT_REPLY   = 0x01
EVT_SUBTYPE_EVENT_REPORT  = 0x02

EVT_PERIODIC = 0x01
EVT_ONLY_FIRST = 0x02

EVT_REQUEST_HEADER_FORMAT_STR = "!BBHI"

EVT_REQUEST_TYPE_ADD = 0x01
EVT_REQUEST_TYPE_MODIFY = 0x02
EVT_REQUEST_TYPE_DELETE = 0x03

EVT_REQUEST_HEADER_SIZE = 8

EVT_PORT_STATS_TIMER_TRIGGER = 0x01
EVT_FLOW_STATS_TIMER_TRIGGER = 0x03

EVT_PORT_TIMER_REQUEST_PACK_STR = "!HHIIQQQQ"

EVT_EVENT_CONDITION_TX_PACKETS = 0x01
EVT_EVENT_CONDITION_TX_BYTES = 0x02
EVT_EVENT_CONDITION_RX_PACKETS = 0x04
EVT_EVENT_CONDITION_RX_BYTES = 0x08

EVT_EVENT_CONDITION_NEW_MATCH_PACKETS = 0x01
EVT_EVENT_CONDITION_NEW_MATCH_BYTES = 0x02
EVT_EVENT_CONDITION_TOTAL_MATCH_PACKETS = 0x04
EVT_EVENT_CONDITION_TOTAL_MATCH_BYTES = 0x08

EVT_EVENT_ID_MAX = 0xffFFff00
EVT_EVENT_ID_ERROR = 0xffFFffEE

EVT_EVENT_REPLY_PACK_STR = "!HHI"
EVT_EVENT_REPLY_SIZE = 8

EVT_EVENT_REPORT_HEADER_PACK_STR = "!HHI"
EVT_EVENT_REPORT_HEADER_SIZE = 8

EVT_PORT_TIMER_REPORT_PACK_STR = "!H2xIIQQQQQQQQ"
EVT_PORT_TIMER_REPORT_SIZE = 56
