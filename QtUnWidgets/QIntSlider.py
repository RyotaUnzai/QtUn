# -*- coding: utf-8 -*-
"""
QIntSlider
web: https://unpyside.com/
e-mail: unpyside@gmail.com

Copyright (c) 2017-2022 UnPySide. All Rights Reserved.

Some of the Docsting is taken or rewritten from the official Qt.
"""
# future
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

# PySide2
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *


# Information about a product --------------------------------------------------
__product__ = "QIntSlider"
__version__ = "0.1.1"
__date__ = "2022-6-26"
__author__ = "Ryota Unzai"
__credits__ = ["Ryota Unzai"]
__maintainer__ = "Ryota Unzai"
__copyright__ = "Copyright (c) 2017-2022 UnPySide. All Rights Reserved."
__email__ = "unpyside@gmail.com"
__license__ = "MIT Licence"
__status__ = "Production"


class QIntSlider(QWidget):
    """QIntSlider widget

    The QIntSlider widget is a widget that displays an int SpinBox and Slider.

    Slots:
        setRange(min, max)
        setValue(value)
        setDirection(direction)
        setOrientation(orientation)
        setValue(value)

    Signals:
        actionTriggered(action)
        rangeChanged(min, max)
        sliderMoved(value)
        sliderPressed()
        sliderReleased()
        valueChanged(value)
    """
    actionTriggered = Signal(int)
    valueChanged = Signal(int)
    sliderPressed = Signal(bool)
    sliderReleased = Signal(bool)
    rangeChanged = Signal(int, int)
    sliderMoved = Signal(int)

    def __init__(self, parent=None, direction=None, *args, **kwargs):
        super(QIntSlider, self).__init__(parent, *args, **kwargs)
        if direction is not None:
            self.__direction = direction
            if self.__direction == QBoxLayout.RightToLeft or self.__direction == QBoxLayout.LeftToRight:
                self.__slider = QSlider(Qt.Horizontal)
            else:
                self.__slider = QSlider(Qt.Vertical)
        else:
            self.__direction = QBoxLayout.LeftToRight
            self.__slider = QSlider(Qt.Horizontal)
        self.__spinBox = QSpinBox()
        self.__layout = QBoxLayout(self.__direction)

        self.__initUI()

    def __initUI(self):
        self.__spinBox.setMinimumWidth(70)
        self.__spinBox.setButtonSymbols(QAbstractSpinBox.NoButtons)

        # spinBox and slider Signals&Slots
        self.__spinBox.valueChanged[int].connect(self.valueChangedCallback)
        self.__slider.valueChanged[int].connect(self.valueChangedCallback)

        # slider Signals&Slots
        self.__slider.actionTriggered[int].connect(self.actionTriggeredCallback)
        self.__slider.sliderPressed.connect(self.sliderPressedCallback)
        self.__slider.sliderReleased.connect(self.sliderReleasedCallback)
        self.__slider.rangeChanged[int, int].connect(self.rangeChangedCallback)
        self.__slider.sliderMoved[int].connect(self.sliderMovedCallback)

        self.__layout.setContentsMargins(0, 0, 0, 0)
        self.__layout.addWidget(self.__spinBox)
        self.__layout.addWidget(self.__slider)
        self.setLayout(self.__layout)

    def setPrefix(self, prefix):
        """This property holds the prefix of the spin box on QIntSlider.
The prefix is prepended to the start of the displayed value. Typical use is to display a unit of measurement or a currency symbol.
To turn off the prefix display, set this property to an empty string. The default is no prefix.
The prefix is not displayed when value() == minimum() and specialValueText() is set.

If no prefix is set, returns an empty string.
        Args:
            prefix (_type_): _description_
        """
        self.__spinBox.setPrefix(prefix)

    def setSuffix(self, suffix):
        """This property holds the suffix of the spin box on QIntSlider.
The suffix is appended to the end of the displayed value. Typical use is to display a unit of measurement or a currency symbol.
To turn off the suffix display, set this property to an empty string. The default is no suffix. The suffix is not displayed for the minimum() if specialValueText() is set.
If no suffix is set, returns an empty string.
        Args:
            suffix (str or unicode): _description_
        """
        self.__spinBox.setSuffix(suffix)

    def setSpecialValueText(self, txt):
        """This property holds the special-value text.
If set, the QIntBox will display this text instead of a numeric value whenever the current value is equal to minimum().
Typical use is to indicate that this choice has a special (default) meaning.

        Args:
            txt (str or unicode): special-value text.
        """
        self.__spinBox.setSpecialValueText(txt)

    def setSingleStep(self, value):
        """This property holds the step value..
The smaller of two natural steps that a QIntslider provides and typically corresponds to the user pressing an arrow key.
If the propety is modified during an auto repeating key event, behavior is undefined.
When a value other than QAbstractSpinBox.NoButtons is set in setButtonSymbols.
When the user uses the arrows to change the spin box's value the value will be incremented/decremented by the amount of the singleStep.
The default value is 1. Setting a singleStep value of less than 0 does nothing.

        Args:
            value (int): _description_
        """
        self.__spinBox.setSingleStep(value)
        self.__slider.setSingleStep(value)

    def value(self):
        """This property holds the value of the QIntSlider.
will emit valueChanged() if the new value is different from the old one.

        Returns:
            int: the value of the QIntSlider
        """
        return self.__spinBox.value()

    def setValue(self, value):
        """This property holds the value of the QIntSlider
will emit valueChanged() if the new calue is different from the old one.

        Parameters:
            value: int
        """
        self.__spinBox.setValue(value)

    def setDirection(self, direction):
        """Sets the direction of this layout to direction.

        QBoxLayout.LeftToRight: Horizontal from left to right.
        QBoxLayout.RightToLeft: Horizontal from right to left.
        QBoxLayout.TopToBottom: Vertical from top to bottom.
        QBoxLayout.BottomToTop: Vertical from bottom to top.

        Args:
            direction (Direction): _description_
        """
        if direction == QBoxLayout.RightToLeft or direction == QBoxLayout.LeftToRight:
            self.__slider.setOrientation(Qt.Horizontal)
        else:
            self.__slider.setOrientation(Qt.Vertical)
        self.__direction = direction
        self.__layout.setDirection(self.__direction)

    def setOrientation(self, orientation):
        """This property holds the orientation of the slider

The orientation must be Qt.Vertical or Qt.Horizontal(the default) .

        Args:
            orientation (orientation): _description_
        """
        self.__slider.setOrientation(orientation)

    def actionTriggeredCallback(self, action):
        self.actionTriggered.emit(action)

    def rangeChangedCallback(self, min, max):
        self.rangeChanged.emit(min, max)

    def sliderMovedCallback(self, value):
        self.sliderMoved.emit(value)

    def sliderPressedCallback(self):
        self.sliderPressed.emit(self.__slider.isSliderDown())

    def sliderReleasedCallback(self):
        self.sliderReleased.emit(self.__slider.isSliderDown())

    def valueChangedCallback(self, value):
        sender = self.sender()
        if sender == self.__spinBox:
            self.__slider.blockSignals(True)
            self.__slider.setValue(value)
            self.__slider.blockSignals(False)
        else:
            self.__spinBox.blockSignals(True)
            self.__spinBox.setValue(value)
            self.__spinBox.blockSignals(False)

        self.valueChanged.emit(value)

    def buttonSymbols(self):
        """This enum type describes the symbols that can be displayed on the buttons in a spin box.

        QAbstractSpinBox.UpDownArrows: Little arrows in the classic style.
        QAbstractSpinBox.PlusMinus: + and - symbols.
        QAbstractSpinBox.NoButtons: Don't display buttons.
        """
        return self.__spinBox.ButtonSymbols()

    def ButtonSymbols(self):
        """This enum type describes the symbols that can be displayed on the buttons in a spin box.

        QAbstractSpinBox.UpDownArrows: Little arrows in the classic style.
        QAbstractSpinBox.PlusMinus: + and - symbols.
        QAbstractSpinBox.NoButtons: Don't display buttons.
        """
        return self.__spinBox.ButtonSymbols()

    def setButtonSymbols(self, bs=QAbstractSpinBox.NoButtons):
        """This property holds the current button symbol mode.
The possible values can be either UpDownArrows or PlusMinus.
The default is NoButtons.
Note that some styles might render PlusMinus and UpDownArrows identically.

        Args:
            bs ButtonSymbols: _description_. Defaults to QAbstractSpinBox.UpDownNoButtonsArrows.
        """
        self.__spinBox.setButtonSymbols(bs)

    def correctionMode(self):
        """This enum type describes the mode the spinbox will use to correct an Intermediate value if editing finishes.

        QAbstractSpinBox.CorrectToPreviousValue: The spinbox will revert to the last valid value.
        QAbstractSpinBox.CorrectToNearestValue: The spinbox will revert to the nearest valid value.
        """
        return self.__spinBox.CorrectionMode()

    def CorrectionMode(self):
        """This enum type describes the mode the spinbox will use to correct an Intermediate value if editing finishes.

        QAbstractSpinBox.CorrectToPreviousValue: The spinbox will revert to the last valid value.
        QAbstractSpinBox.CorrectToNearestValue: The spinbox will revert to the nearest valid value.
        """
        return self.__spinBox.CorrectionMode()

    def setCorrectionMode(self, cm=QAbstractSpinBox.CorrectToPreviousValue):
        """This property holds the mode to correct an Intermediate value if editing finishes.
The default mode is CorrectToPreviousValue.

        Args:
            cm (CorrectionMode): _description_. Defaults to QAbstractSpinBox.CorrectToPreviousValue.
        """
        self.__spinBox.setCorrectionMode(cm)

    def setRange(self, min, max):
        """Convenience function to set the minimum, and maximum values with a single function call.

        Args:
            min (int): minimum value
            max (int): maximum value
        """
        self.__spinBox.setRange(min, max)
        self.__slider.setRange(min, max)


"""
TODO: Selection of what to implement and what not to implement, and implementation of selected functions.
    def PlusMinus(self):
        pass

    def RenderFlag(self):
        pass

    def RenderFlags(self):
        pass

    def SliderAction(self):
        pass

    def SliderChange(self):
        pass

    def SliderMove(self):
        pass

    def SliderNoAction(self):
        pass

    def SliderOrientationChange(self):
        pass

    def SliderPageStepAdd(self):
        pass

    def SliderPageStepSub(self):
        pass

    def SliderRangeChange(self):
        pass

    def SliderSingleStepAdd(self):
        pass

    def SliderSingleStepSub(self):
        pass

    def SliderStepsChange(self):
        pass

    def SliderToMaximum(self):
        pass

    def SliderToMinimum(self):
        pass

    def SliderValueChange(self):
        pass

    def StepDownEnabled(self):
        pass

    def StepEnabled(self):
        pass

    def StepNone(self):
        pass

    def StepUpEnabled(self):
        pass

    def TickPosition(self):
        pass

    def TicksAbove(self):
        pass

    def TicksBelow(self):
        pass

    def TicksBothSides(self):
        pass

    def TicksLeft(self):
        pass

    def TicksRight(self):
        pass

    def UpDownArrows(self):
        pass

    def acceptDrops(self):
        pass

    def accessibleDescription(self):
        pass

    def accessibleName(self):
        pass

    def actionEvent(self):
        pass

    def actionTriggered(self):
        pass

    def actions(self):
        pass

    def activateWindow(self):
        pass

    def addAction(self):
        pass

    def addActions(self):
        pass

    def adjustSize(self):
        pass

    def alignment(self):
        pass

    def autoFillBackground(self):
        pass

    def backgroundRole(self):
        pass

    def baseSize(self):
        pass

    def blockSignals(self):
        pass

    def buttonSymbols(self):
        pass

    def changeEvent(self):
        pass

    def childAt(self):
        pass

    def childEvent(self):
        pass

    def children(self):
        pass

    def childrenRect(self):
        pass

    def childrenRegion(self):
        pass

    def cleanText(self):
        pass

    def clear(self):
        pass

    def clearFocus(self):
        pass

    def clearMask(self):
        pass

    def close(self):
        pass

    def closeEvent(self):
        pass

    def colorCount(self):
        pass

    def connect(self):
        pass

    def connectNotify(self):
        pass

    def contentsMargins(self):
        pass

    def contentsRect(self):
        pass

    def contextMenuEvent(self):
        pass

    def contextMenuPolicy(self):
        pass

    def correctionMode(self):
        pass

    def create(self):
        pass

    def createWinId(self):
        pass

    def createWindowContainer(self):
        pass

    def cursor(self):
        pass

    def customContextMenuRequested(self):
        pass

    def customEvent(self):
        pass

    def deleteLater(self):
        pass

    def depth(self):
        pass

    def destroy(self):
        pass

    def destroyed(self):
        pass

    def devType(self):
        pass

    def devicePixelRatio(self):
        pass

    def devicePixelRatioF(self):
        pass

    def devicePixelRatioFScale(self):
        pass

    def disconnect(self):
        pass

    def disconnectNotify(self):
        pass

    def displayIntegerBase(self):
        pass

    def dragEnterEvent(self):
        pass

    def dragLeaveEvent(self):
        pass

    def dragMoveEvent(self):
        pass

    def dropEvent(self):
        pass

    def dumpObjectInfo(self):
        pass

    def dumpObjectTree(self):
        pass

    def dynamicPropertyNames(self):
        pass

    def editingFinished(self):
        pass

    def effectiveWinId(self):
        pass

    def emit(self):
        pass

    def ensurePolished(self):
        pass

    def enterEvent(self):
        pass

    def event(self):
        pass

    def eventFilter(self):
        pass

    def find(self):
        pass

    def findChild(self):
        pass

    def findChildren(self):
        pass

    def fixup(self):
        pass

    def focusInEvent(self):
        pass

    def focusNextChild(self):
        pass

    def focusNextPrevChild(self):
        pass

    def focusOutEvent(self):
        pass

    def focusPolicy(self):
        pass

    def focusPreviousChild(self):
        pass

    def focusProxy(self):
        pass

    def focusWidget(self):
        pass

    def font(self):
        pass

    def fontInfo(self):
        pass

    def fontMetrics(self):
        pass

    def foregroundRole(self):
        pass

    def frameGeometry(self):
        pass

    def frameSize(self):
        pass

    def geometry(self):
        pass

    def getContentsMargins(self):
        pass

    def grab(self):
        pass

    def grabGesture(self):
        pass

    def grabKeyboard(self):
        pass

    def grabMouse(self):
        pass

    def grabShortcut(self):
        pass

    def graphicsEffect(self):
        pass

    def graphicsProxyWidget(self):
        pass

    def hasAcceptableInput(self):
        pass

    def hasFocus(self):
        pass

    def hasFrame(self):
        pass

    def hasHeightForWidth(self):
        pass

    def hasMouseTracking(self):
        pass

    def hasTracking(self):
        pass

    def height(self):
        pass

    def heightForWidth(self):
        pass

    def heightMM(self):
        pass

    def hide(self):
        pass

    def hideEvent(self):
        pass

    def inherits(self):
        pass

    def initPainter(self):
        pass

    def initStyleOption(self):
        pass

    def inputMethodEvent(self):
        pass

    def inputMethodHints(self):
        pass

    def inputMethodQuery(self):
        pass

    def insertAction(self):
        pass

    def insertActions(self):
        pass

    def installEventFilter(self):
        pass

    def internalWinId(self):
        pass

    def interpretText(self):
        pass

    def invertedAppearance(self):
        pass

    def invertedControls(self):
        pass

    def isAccelerated(self):
        pass

    def isActiveWindow(self):
        pass

    def isAncestorOf(self):
        pass

    def isEnabled(self):
        pass

    def isEnabledTo(self):
        pass

    def isEnabledToTLW(self):
        pass

    def isFullScreen(self):
        pass

    def isGroupSeparatorShown(self):
        pass

    def isHidden(self):
        pass

    def isLeftToRight(self):
        pass

    def isMaximized(self):
        pass

    def isMinimized(self):
        pass

    def isModal(self):
        pass

    def isReadOnly(self):
        pass

    def isRightToLeft(self):
        pass

    def isSignalConnected(self):
        pass

    def isSliderDown(self):
        pass

    def isTopLevel(self):
        pass

    def isVisible(self):
        pass

    def isVisibleTo(self):
        pass

    def isWidgetType(self):
        pass

    def isWindow(self):
        pass

    def isWindowModified(self):
        pass

    def isWindowType(self):
        pass

    def keyPressEvent(self):
        pass

    def keyReleaseEvent(self):
        pass

    def keyboardGrabber(self):
        pass

    def keyboardTracking(self):
        pass

    def killTimer(self):
        pass

    def layout(self):
        pass

    def layoutDirection(self):
        pass

    def leaveEvent(self):
        pass

    def lineEdit(self):
        pass

    def locale(self):
        pass

    def logicalDpiX(self):
        pass

    def logicalDpiY(self):
        pass

    def lower(self):
        pass

    def mapFrom(self):
        pass

    def mapFromGlobal(self):
        pass

    def mapFromParent(self):
        pass

    def mapTo(self):
        pass

    def mapToGlobal(self):
        pass

    def mapToParent(self):
        pass

    def mask(self):
        pass

    def maximum(self):
        pass

    def maximumHeight(self):
        pass

    def maximumSize(self):
        pass

    def maximumWidth(self):
        pass

    def metaObject(self):
        pass

    def metric(self):
        pass

    def minimum(self):
        pass

    def minimumHeight(self):
        pass

    def minimumSize(self):
        pass

    def minimumSizeHint(self):
        pass

    def minimumWidth(self):
        pass

    def mouseDoubleClickEvent(self):
        pass

    def mouseGrabber(self):
        pass

    def mouseMoveEvent(self):
        pass

    def mousePressEvent(self):
        pass

    def mouseReleaseEvent(self):
        pass

    def move(self):
        pass

    def moveEvent(self):
        pass

    def moveToThread(self):
        pass

    def nativeParentWidget(self):
        pass

    def nextInFocusChain(self):
        pass

    def normalGeometry(self):
        pass

    def objectName(self):
        pass

    def objectNameChanged(self):
        pass

    def orientation(self):
        pass

    def overrideWindowFlags(self):
        pass

    def overrideWindowState(self):
        pass

    def pageStep(self):
        pass

    def paintEngine(self):
        pass

    def paintEvent(self):
        pass

    def painters(self):
        pass

    def paintingActive(self):
        pass

    def palette(self):
        pass

    def parent(self):
        pass

    def parentWidget(self):
        pass

    def physicalDpiX(self):
        pass

    def physicalDpiY(self):
        pass

    def pos(self):
        pass

    def prefix(self):
        pass

    def previousInFocusChain(self):
        pass

    def property(self):
        pass

    def raise_(self):
        pass

    def rangeChanged(self):
        pass

    def receivers(self):
        pass

    def rect(self):
        pass

    def redirected(self):
        pass

    def registerUserData(self):
        pass

    def releaseKeyboard(self):
        pass

    def releaseMouse(self):
        pass

    def releaseShortcut(self):
        pass

    def removeAction(self):
        pass

    def removeEventFilter(self):
        pass

    def render(self):
        pass

    def repaint(self):
        pass

    def repeatAction(self):
        pass

    def resize(self):
        pass

    def resizeEvent(self):
        pass

    def restoreGeometry(self):
        pass

    def saveGeometry(self):
        pass

    def scroll(self):
        pass

    def selectAll(self):
        pass

    def sender(self):
        pass

    def senderSignalIndex(self):
        pass

    def setAccelerated(self):
        pass

    def setAcceptDrops(self):
        pass

    def setAccessibleDescription(self):
        pass

    def setAccessibleName(self):
        pass

    def setAlignment(self):
        pass

    def setAttribute(self):
        pass

    def setAutoFillBackground(self):
        pass

    def setBackgroundRole(self):
        pass

    def setBaseSize(self):
        pass

    def setButtonSymbols(self):
        pass

    def setContentsMargins(self):
        pass

    def setContextMenuPolicy(self):
        pass

    def setCursor(self):
        pass

    def setDisabled(self):
        pass

    def setDisplayIntegerBase(self):
        pass

    def setEnabled(self):
        pass

    def setFixedHeight(self):
        pass

    def setFixedSize(self):
        pass

    def setFixedWidth(self):
        pass

    def setFocus(self):
        pass

    def setFocusPolicy(self):
        pass

    def setFocusProxy(self):
        pass

    def setFont(self):
        pass

    def setForegroundRole(self):
        pass

    def setFrame(self):
        pass

    def setGeometry(self):
        pass

    def setGraphicsEffect(self):
        pass

    def setGroupSeparatorShown(self):
        pass

    def setHidden(self):
        pass

    def setInputMethodHints(self):
        pass

    def setInvertedAppearance(self):
        pass

    def setInvertedControls(self):
        pass

    def setKeyboardTracking(self):
        pass

    def setLayoutDirection(self):
        pass

    def setLineEdit(self):
        pass

    def setLocale(self):
        pass

    def setMask(self):
        pass

    def setMaximum(self):
        pass

    def setMaximumHeight(self):
        pass

    def setMaximumSize(self):
        pass

    def setMaximumWidth(self):
        pass

    def setMinimum(self):
        pass

    def setMinimumHeight(self):
        pass

    def setMinimumSize(self):
        pass

    def setMinimumWidth(self):
        pass

    def setMouseTracking(self):
        pass

    def setObjectName(self):
        pass

    def setOrientation(self):
        pass

    def setPageStep(self):
        pass

    def setPalette(self):
        pass

    def setParent(self):
        pass

    def setPrefix(self):
        pass

    def setProperty(self):
        pass

    def setRange(self):
        pass

    def setReadOnly(self):
        pass

    def setRepeatAction(self):
        pass

    def setShortcutAutoRepeat(self):
        pass

    def setShortcutEnabled(self):
        pass

    def setSingleStep(self):
        pass

    def setSizeIncrement(self):
        pass

    def setSizePolicy(self):
        pass

    def setSliderDown(self):
        pass

    def setSliderPosition(self):
        pass

    def setSpecialValueText(self):
        pass

    def setStatusTip(self):
        pass

    def setStyle(self):
        pass

    def setStyleSheet(self):
        pass

    def setSuffix(self):
        pass

    def setTabOrder(self):
        pass

    def setTickInterval(self):
        pass

    def setTickPosition(self):
        pass

    def setToolTip(self):
        pass

    def setToolTipDuration(self):
        pass

    def setTracking(self):
        pass

    def setUpdatesEnabled(self):
        pass

    def setValue(self):
        pass

    def setVisible(self):
        pass

    def setWhatsThis(self):
        pass

    def setWindowFilePath(self):
        pass

    def setWindowFlags(self):
        pass

    def setWindowIcon(self):
        pass

    def setWindowIconText(self):
        pass

    def setWindowModality(self):
        pass

    def setWindowModified(self):
        pass

    def setWindowOpacity(self):
        pass

    def setWindowRole(self):
        pass

    def setWindowState(self):
        pass

    def setWindowTitle(self):
        pass

    def setWrapping(self):
        pass

    def sharedPainter(self):
        pass

    def show(self):
        pass

    def showEvent(self):
        pass

    def showFullScreen(self):
        pass

    def showMaximized(self):
        pass

    def showMinimized(self):
        pass

    def showNormal(self):
        pass

    def signalsBlocked(self):
        pass

    def singleStep(self):
        pass

    def size(self):
        pass

    def sizeHint(self):
        pass

    def sizeIncrement(self):
        pass

    def sizePolicy(self):
        pass

    def sliderChange(self):
        pass

    def sliderMoved(self):
        pass

    def sliderPosition(self):
        pass

    def sliderPressed(self):
        pass

    def sliderReleased(self):
        pass

    def specialValueText(self):
        pass

    def stackUnder(self):
        pass

    def startTimer(self):
        pass

    def staticMetaObject(self):
        pass

    def statusTip(self):
        pass

    def stepBy(self):
        pass

    def stepDown(self):
        pass

    def stepEnabled(self):
        pass

    def stepUp(self):
        pass

    def style(self):
        pass

    def styleSheet(self):
        pass

    def suffix(self):
        pass

    def tabletEvent(self):
        pass

    def testAttribute(self):
        pass

    def text(self):
        pass

    def textFromValue(self):
        pass

    def thread(self):
        pass

    def tickInterval(self):
        pass

    def tickPosition(self):
        pass

    def timerEvent(self):
        pass

    def toolTip(self):
        pass

    def toolTipDuration(self):
        pass

    def topLevelWidget(self):
        pass

    def tr(self):
        pass

    def triggerAction(self):
        pass

    def underMouse(self):
        pass

    def ungrabGesture(self):
        pass

    def unsetCursor(self):
        pass

    def unsetLayoutDirection(self):
        pass

    def unsetLocale(self):
        pass

    def update(self):
        pass

    def updateGeometry(self):
        pass

    def updateMicroFocus(self):
        pass

    def updatesEnabled(self):
        pass

    def validate(self):
        pass

    def value(self):
        pass

    def valueChanged(self):
        pass

    def valueFromText(self):
        pass

    def visibleRegion(self):
        pass

    def whatsThis(self):
        pass

    def wheelEvent(self):
        pass

    def width(self):
        pass

    def widthMM(self):
        pass

    def winId(self):
        pass

    def window(self):
        pass

    def windowFilePath(self):
        pass

    def windowFlags(self):
        pass

    def windowHandle(self):
        pass

    def windowIcon(self):
        pass

    def windowIconChanged(self):
        pass

    def windowIconText(self):
        pass

    def windowIconTextChanged(self):
        pass

    def windowModality(self):
        pass

    def windowOpacity(self):
        pass

    def windowRole(self):
        pass

    def windowState(self):
        pass

    def windowTitle(self):
        pass

    def windowTitleChanged(self):
        pass

    def windowType(self):
        pass

    def wrapping(self):
        pass

    def x(self):
        pass

    def y(self):
        pass
"""
