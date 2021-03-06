# automatically generated by the FlatBuffers compiler, do not modify

# namespace: flatbuffers

import flatbuffers

class WidgetOptions(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsWidgetOptions(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = WidgetOptions()
        x.Init(buf, n + offset)
        return x

    # WidgetOptions
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # WidgetOptions
    def Name(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # WidgetOptions
    def ActionTag(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # WidgetOptions
    def RotationSkew(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            x = o + self._tab.Pos
            from .RotationSkew import RotationSkew
            obj = RotationSkew()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # WidgetOptions
    def ZOrder(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # WidgetOptions
    def Visible(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return True

    # WidgetOptions
    def Alpha(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, o + self._tab.Pos)
        return 255

    # WidgetOptions
    def Tag(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # WidgetOptions
    def Position(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            x = o + self._tab.Pos
            from .Position import Position
            obj = Position()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # WidgetOptions
    def Scale(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            x = o + self._tab.Pos
            from .Scale import Scale
            obj = Scale()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # WidgetOptions
    def AnchorPoint(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            x = o + self._tab.Pos
            from .AnchorPoint import AnchorPoint
            obj = AnchorPoint()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # WidgetOptions
    def Color(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            x = o + self._tab.Pos
            from .Color import Color
            obj = Color()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # WidgetOptions
    def Size(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            x = o + self._tab.Pos
            from .FlatSize import FlatSize
            obj = FlatSize()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # WidgetOptions
    def FlipX(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(28))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

    # WidgetOptions
    def FlipY(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(30))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

    # WidgetOptions
    def IgnoreSize(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(32))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

    # WidgetOptions
    def TouchEnabled(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(34))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

    # WidgetOptions
    def FrameEvent(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(36))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # WidgetOptions
    def CustomProperty(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(38))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # WidgetOptions
    def CallBackType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(40))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # WidgetOptions
    def CallBackName(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(42))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # WidgetOptions
    def LayoutComponent(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(44))
        if o != 0:
            x = self._tab.Indirect(o + self._tab.Pos)
            from .LayoutComponentTable import LayoutComponentTable
            obj = LayoutComponentTable()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

def WidgetOptionsStart(builder): builder.StartObject(21)
def WidgetOptionsAddName(builder, name): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(name), 0)
def WidgetOptionsAddActionTag(builder, actionTag): builder.PrependInt32Slot(1, actionTag, 0)
def WidgetOptionsAddRotationSkew(builder, rotationSkew): builder.PrependStructSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(rotationSkew), 0)
def WidgetOptionsAddZOrder(builder, zOrder): builder.PrependInt32Slot(3, zOrder, 0)
def WidgetOptionsAddVisible(builder, visible): builder.PrependBoolSlot(4, visible, 1)
def WidgetOptionsAddAlpha(builder, alpha): builder.PrependUint8Slot(5, alpha, 255)
def WidgetOptionsAddTag(builder, tag): builder.PrependInt32Slot(6, tag, 0)
def WidgetOptionsAddPosition(builder, position): builder.PrependStructSlot(7, flatbuffers.number_types.UOffsetTFlags.py_type(position), 0)
def WidgetOptionsAddScale(builder, scale): builder.PrependStructSlot(8, flatbuffers.number_types.UOffsetTFlags.py_type(scale), 0)
def WidgetOptionsAddAnchorPoint(builder, anchorPoint): builder.PrependStructSlot(9, flatbuffers.number_types.UOffsetTFlags.py_type(anchorPoint), 0)
def WidgetOptionsAddColor(builder, color): builder.PrependStructSlot(10, flatbuffers.number_types.UOffsetTFlags.py_type(color), 0)
def WidgetOptionsAddSize(builder, size): builder.PrependStructSlot(11, flatbuffers.number_types.UOffsetTFlags.py_type(size), 0)
def WidgetOptionsAddFlipX(builder, flipX): builder.PrependBoolSlot(12, flipX, 0)
def WidgetOptionsAddFlipY(builder, flipY): builder.PrependBoolSlot(13, flipY, 0)
def WidgetOptionsAddIgnoreSize(builder, ignoreSize): builder.PrependBoolSlot(14, ignoreSize, 0)
def WidgetOptionsAddTouchEnabled(builder, touchEnabled): builder.PrependBoolSlot(15, touchEnabled, 0)
def WidgetOptionsAddFrameEvent(builder, frameEvent): builder.PrependUOffsetTRelativeSlot(16, flatbuffers.number_types.UOffsetTFlags.py_type(frameEvent), 0)
def WidgetOptionsAddCustomProperty(builder, customProperty): builder.PrependUOffsetTRelativeSlot(17, flatbuffers.number_types.UOffsetTFlags.py_type(customProperty), 0)
def WidgetOptionsAddCallBackType(builder, callBackType): builder.PrependUOffsetTRelativeSlot(18, flatbuffers.number_types.UOffsetTFlags.py_type(callBackType), 0)
def WidgetOptionsAddCallBackName(builder, callBackName): builder.PrependUOffsetTRelativeSlot(19, flatbuffers.number_types.UOffsetTFlags.py_type(callBackName), 0)
def WidgetOptionsAddLayoutComponent(builder, layoutComponent): builder.PrependUOffsetTRelativeSlot(20, flatbuffers.number_types.UOffsetTFlags.py_type(layoutComponent), 0)
def WidgetOptionsEnd(builder): return builder.EndObject()
